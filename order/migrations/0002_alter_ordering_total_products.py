# Generated by Django 4.1.6 on 2023-02-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordering",
            name="total_products",
            field=models.IntegerField(max_length=30),
        ),
    ]
