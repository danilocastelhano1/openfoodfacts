import logging

from celery import shared_task

from coodesh.api.scrappers.open_food import run_scrapper

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def scrap_products(self):
    """
    Task to run ever X days to get the products information
    """
    try:
        run_scrapper()
        return "Scrapper ran successfully"
    except Exception as err:
        logger.exception("Exception executing scrapper, error: %s", err)
        return f"Exception, {err}"
