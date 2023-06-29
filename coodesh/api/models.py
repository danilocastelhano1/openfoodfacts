import uuid

from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from model_utils import Choices

StatusChoices = Choices(
    ("draft", "DRAFT", "draft"),
    ("imported", "IMPORTED", "imported"),
)


# Create your models here.
class BaseModel(models.Model):
    """
    Base model to be used in the models containing common fields
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Id"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        abstract = True
        indexes = [BrinIndex(fields=["created_at"])]


class Product(BaseModel):
    """
    given a json example, I've created a model to store the information
    about the products
    """

    code = models.CharField(max_length=800, blank=False, null=False)
    barcode = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(
        max_length=25, blank=False, null=False, choices=StatusChoices
    )
    imported_t = models.DateTimeField(auto_now_add=True, verbose_name="Updated at")
    url = models.CharField(max_length=800, blank=True, null=True)
    product_name = models.CharField(max_length=800, blank=True, null=True)
    quantity = models.CharField(max_length=800, blank=True, null=True)
    categories = models.TextField(blank=True, null=True)
    packaging = models.TextField(blank=True, null=True)
    brands = models.TextField(blank=True, null=True)
    image_url = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.code} - {self.product_name}"


class Alert(BaseModel):
    """
    Model to stores errors in scrap routine
    """

    error = models.TextField(blank=False, null=False)
