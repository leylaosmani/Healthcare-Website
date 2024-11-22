# Generated by Django 5.1.3 on 2024-11-22 02:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
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
                ("date", models.DateTimeField()),
                ("reason", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Scheduled", "Scheduled"),
                            ("Completed", "Completed"),
                            ("Cancelled", "Cancelled"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointments_as_doctor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointments_as_patient",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
