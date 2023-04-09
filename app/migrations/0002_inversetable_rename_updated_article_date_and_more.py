# Generated by Django 4.1.5 on 2023-02-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
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
                ("location", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name="article",
            old_name="updated",
            new_name="date",
        ),
        migrations.RenameField(
            model_name="article",
            old_name="site_name",
            new_name="writer",
        ),
        migrations.RemoveField(
            model_name="article",
            name="plus",
        ),
        migrations.AddField(
            model_name="article",
            name="content",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="content_noun",
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="href",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="title_noun",
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="관람",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="대회",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="업체",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="의견수렴",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="의회",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="전문교육",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="전체교육",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="주민자치",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="채용",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="청소년",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="합격자",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="행사",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
