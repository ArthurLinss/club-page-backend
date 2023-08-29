# Generated by Django 4.2.4 on 2023-08-08 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orga", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=255)),
                ("number", models.CharField(max_length=20)),
                ("country", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="orga.address",
            ),
        ),
    ]