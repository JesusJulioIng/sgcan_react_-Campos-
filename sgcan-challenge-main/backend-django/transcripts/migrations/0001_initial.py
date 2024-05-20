# Generated by Django 5.0.6 on 2024-05-17 18:31

import django.core.serializers.json
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transcript",
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
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("date", models.DateTimeField(blank=True, default=None, null=True)),
                ("duration", models.IntegerField(blank=True, null=True)),
                (
                    "summary",
                    models.JSONField(
                        blank=True,
                        encoder=django.core.serializers.json.DjangoJSONEncoder,
                        null=True,
                    ),
                ),
                ("video_url", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sentence",
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
                ("index", models.IntegerField(blank=True, db_index=True, null=True)),
                ("text", models.TextField(blank=True, null=True)),
                ("start_time", models.CharField(blank=True, max_length=255, null=True)),
                ("end_time", models.CharField(blank=True, max_length=255, null=True)),
                ("speaker_id", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "speaker_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "transcript",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sentences",
                        to="transcripts.transcript",
                    ),
                ),
            ],
            options={
                "ordering": ["index"],
            },
        ),
    ]
