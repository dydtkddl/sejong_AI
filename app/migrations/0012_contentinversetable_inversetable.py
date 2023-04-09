# Generated by Django 4.1.5 on 2023-02-03 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0011_delete_contentinversetable_delete_inversetable"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContentInverseTable",
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
                ("word", models.CharField(max_length=100, null=True)),
                ("frequency", models.IntegerField(null=True)),
                ("location", models.TextField(max_length=200000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="InverseTable",
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
                ("word", models.CharField(max_length=100, null=True)),
                ("frequency", models.IntegerField(null=True)),
                ("location", models.TextField(max_length=200000, null=True)),
            ],
        ),
    ]
