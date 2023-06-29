from rest_framework import serializers

from coodesh.api.models import Product


class ProductsSerializer(serializers.ModelSerializer):
    """
    Fields to be shown in the view
    """

    class Meta:
        model = Product
        fields = (
            "code",
            "barcode",
            "status",
            "imported_t",
            "url",
            "product_name",
            "quantity",
            "categories",
            "packaging",
            "brands",
            "image_url",
        )
        read_only_fields = ("id", "created_at", "updated_at")
