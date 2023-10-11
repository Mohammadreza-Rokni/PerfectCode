# Generated by Django 4.1.3 on 2023-01-24 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0001_initial"),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="category.category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="زمان ایجاد"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(max_length=250, null=True, verbose_name="توضیحات"),
        ),
        migrations.AlterField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(
                blank=True, default=True, null=True, verbose_name="فعال"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=50, null=True, verbose_name="عنوان"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.CharField(max_length=50, null=True, verbose_name="قیمت"),
        ),
        migrations.AlterField(
            model_name="product",
            name="stock",
            field=models.IntegerField(default=0, null=True, verbose_name="تعداد موجود"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="زمان به روز رسانی"
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, null=True, verbose_name="نام کاربر"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, null=True, verbose_name="ادرس الکترونیکی"
                    ),
                ),
                ("massage", models.TextField(null=True, verbose_name="متن نظر")),
                (
                    "date",
                    models.DateField(
                        auto_now_add=True, null=True, verbose_name="تاریخ ثبت"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
            options={
                "verbose_name": " نظر ",
                "verbose_name_plural": " نظرات ",
            },
        ),
    ]
