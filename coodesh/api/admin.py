from django.contrib import admin

from coodesh.api.models import Alert
from coodesh.api.models import Product

"""
Registering the models to be available into django admin
"""
admin.site.register(Product)
admin.site.register(Alert)
