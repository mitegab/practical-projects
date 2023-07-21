# Generated by Django 4.2.1 on 2023-05-22 10:24

from django.db import migrations


def set_default_none(apps, schema_editor):
    Podcast = apps.get_model("podcasts", "Podcast")
    Podcast.objects.filter(parser_result="success").update(parser_result=None)


class Migration(migrations.Migration):
    dependencies = [
        ("podcasts", "0032_alter_podcast_parser_result"),
    ]

    operations = [
        migrations.RunPython(set_default_none, reverse_code=migrations.RunPython.noop)
    ]