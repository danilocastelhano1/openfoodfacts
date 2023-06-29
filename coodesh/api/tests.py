from rest_framework import status
from rest_framework.test import APITestCase

from coodesh.api.models import Product
from coodesh.api.models import StatusChoices


class ApiProductsTests(APITestCase):
    def test_index(self):
        resp = self.client.get("")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, "Fullstack Challenge 20201026")

    def test_list_products(self):
        Product.objects.create(
            code="123",
            barcode="456",
            status=StatusChoices.DRAFT,
            url="https://127.0.0.1/123456",
            product_name="test case",
            quantity="2kg",
            categories="water",
            packaging="bottle",
            brands="nestlé",
            image_url="https://127.0.0.1/images/123456",
        )
        Product.objects.create(
            code="999",
            barcode="888",
            status=StatusChoices.IMPORTED,
            url="https://127.0.0.1/999888",
            product_name="test case",
            quantity="2kg",
            categories="soda",
            packaging="can",
            brands="pepsi",
            image_url="https://127.0.0.1/images/999888",
        )

        resp = self.client.get("/products/")
        json = resp.json()

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(json["count"], 2)

    def test_retrieve_products_success(self):
        Product.objects.create(
            code="123",
            barcode="456",
            status=StatusChoices.DRAFT,
            url="https://127.0.0.1/123456",
            product_name="test case",
            quantity="2kg",
            categories="water",
            packaging="bottle",
            brands="nestlé",
            image_url="https://127.0.0.1/images/123456",
        )

        resp = self.client.get("/products/123/")
        json = resp.json()

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(json)

    def test_retrieve_products_error(self):
        resp = self.client.get("/products/xxxx/")
        json = resp.json()

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(json, {"detail": "Not Found"})
