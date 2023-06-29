import logging

from datetime import datetime
from typing import Any
from typing import Union

import requests

from bs4 import BeautifulSoup
from django.conf import settings
from requests.adapters import HTTPAdapter
from requests.adapters import Retry

from coodesh.api.models import Alert
from coodesh.api.models import Product
from coodesh.api.models import StatusChoices

logger = logging.getLogger(__name__)


def run_scrapper():
    """
    Public method to run the scrapper
    """
    logger.info("Starting task open_food_scrapper in {}".format(datetime.now()))
    __open_food_scrapper()
    logger.info("Finishing task open_food_scrapper in {}".format(datetime.now()))


def __get_field_or_none(soup_item: Any, field_id: str) -> Union[str, None]:
    """
    Some products do not have some fields, in this method I treat this
    and if exists I return the value, if don't return None
    """
    try:
        return soup_item.find(id=field_id).get_text()
    except AttributeError:
        return None


def __open_food_scrapper() -> None:
    """
    Method to swipe the site https://world.openfoodfacts.org
    get the products and store its products into Product Model
    """
    try:
        request_session = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        request_session.mount("https://", HTTPAdapter(max_retries=retries))

        html = request_session.get("https://world.openfoodfacts.org/").content
        soup = BeautifulSoup(html, "html.parser")

        products = (
            soup.find(id="search_results")
            .find_next("ul")
            .find_all("li")[: settings.QT_ITEMS_TO_SCRAP]
        )

        list_count: int = 1
        for product in products:
            link = (
                f"https://world.openfoodfacts.org{product.find('a', href=True)['href']}"
            )
            code: str = link.split("/")[5]

            if Product.objects.filter(code=code).exists():
                continue

            html_item = request_session.get(link).content
            soup_item = BeautifulSoup(html_item, "html.parser")
            barcode: str = (
                soup_item.find(id="barcode_paragraph").get_text(
                    separator=" ", strip=True
                )
                if soup_item.find(id="barcode_paragraph")
                else None
            )
            status: str = StatusChoices.IMPORTED
            url: str = link
            product_name: str = (
                soup_item.find("h2", class_="title-1")
                .get_text(separator="/", strip=True)
                .split("/")[0]
            )
            quantity: str = __get_field_or_none(soup_item, "field_quantity_value")
            categories: str = __get_field_or_none(soup_item, "field_categories_value")
            packaging: str = __get_field_or_none(soup_item, "field_packaging_value")
            brands: str = __get_field_or_none(soup_item, "field_brands_value")
            image_url: str = (
                soup_item.find(id="og_image")["src"]
                if soup_item.find(id="og_image") is not None
                else None
            )

            logger.info("Adding product to list %d / %d", list_count, len(products))
            Product.objects.create(
                code=code,
                barcode=barcode,
                status=status,
                url=url,
                product_name=product_name,
                quantity=quantity,
                categories=categories,
                packaging=packaging,
                brands=brands,
                image_url=image_url,
            )

            list_count += 1
    except Exception as err:
        logger.error(f"Scrapping error: {str(err)}")
        """
        Creates an Alert with his error
        """
        Alert.objects.create(error=str(err))
        raise err
