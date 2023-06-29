from django.urls import include
from django.urls import path
from rest_framework import routers

from coodesh.api.views import Index
from coodesh.api.views import ProductsViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductsViewSet, basename="products")

urlpatterns = [
    path(r"", Index.as_view(), name="index"),
    path(r"", include(router.urls)),
]
