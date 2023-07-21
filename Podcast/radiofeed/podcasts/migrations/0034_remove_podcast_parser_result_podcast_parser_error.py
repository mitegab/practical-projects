# Generated by Django 4.2.1 on 2023-05-22 10:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("podcasts", "0033_set_parser_result_none"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="podcast",
            name="parser_result",
        ),
        migrations.AddField(
            model_name="podcast",
            name="parser_error",
            field=models.CharField(
                blank=True,
                choices=[
                    ("duplicate", "Duplicate"),
                    ("inaccessible", "Inaccessible"),
                    ("invalid_rss", "Invalid RSS"),
                    ("not_modified", "Not Modified"),
                    ("unavailable", "Unavailable"),
                ],
                max_length=30,
                null=True,
            ),
        ),
    ]