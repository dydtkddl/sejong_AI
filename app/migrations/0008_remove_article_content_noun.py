# Generated by Django 4.1.5 on 2023-02-03 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_contentinversetable_inversetable"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="content_noun",
        ),
    ]