# Generated by Django 4.1.7 on 2023-03-06 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_product_featured"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="Category",
            new_name="category",
        ),
    ]
