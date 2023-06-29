from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from coodesh.api.models import Product
from coodesh.api.serializers import ProductsSerializer


class Index(APIView):
    def get(self, request):
        return Response("Fullstack Challenge 20201026")


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        """
        By default, Django finds his data by pk, here i'm changing that
        to looks into code and not pk
        """
        queryset = self.get_queryset().filter(code=kwargs["pk"]).first()
        if not queryset:
            return Response({"detail": "Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ProductsSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
