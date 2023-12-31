# Generated by Django 4.2.2 on 2023-06-29 14:47

import uuid

import django.contrib.postgres.indexes

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("code", models.CharField(max_length=800)),
                ("barcode", models.CharField(blank=True, max_length=120, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "draft"), ("imported", "imported")],
                        max_length=25,
                    ),
                ),
                (
                    "imported_t",
                    models.DateTimeField(auto_now_add=True, verbose_name="Updated at"),
                ),
                ("url", models.CharField(blank=True, max_length=800, null=True)),
                (
                    "product_name",
                    models.CharField(blank=True, max_length=800, null=True),
                ),
                ("quantity", models.CharField(blank=True, max_length=800, null=True)),
                ("categories", models.TextField(blank=True, null=True)),
                ("packaging", models.TextField(blank=True, null=True)),
                ("brands", models.TextField(blank=True, null=True)),
                ("image_url", models.CharField(blank=True, max_length=800, null=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Alert",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("error", models.TextField()),
            ],
            options={
                "abstract": False,
                "indexes": [
                    django.contrib.postgres.indexes.BrinIndex(
                        fields=["created_at"], name="api_alert_created_87638a_brin"
                    )
                ],
            },
        ),
    ]
