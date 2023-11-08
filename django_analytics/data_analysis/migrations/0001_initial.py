# Generated by Django 4.2.6 on 2023-11-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cars",
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
                ("model", models.CharField(max_length=50)),
                ("year", models.IntegerField()),
                ("price", models.FloatField()),
                ("transmission", models.CharField(max_length=255)),
                ("mileage", models.IntegerField()),
                ("fuel_type", models.CharField(max_length=255)),
                ("tax", models.FloatField()),
                ("mpg", models.FloatField()),
                ("engine_size", models.FloatField()),
                ("make", models.CharField(max_length=255)),
            ],
        ),
    ]
