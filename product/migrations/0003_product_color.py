# Generated by Django 4.1.3 on 2023-01-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_category_alter_product_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=50, null=True, verbose_name='رنگ'),
        ),
    ]
