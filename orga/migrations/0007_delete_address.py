# Generated by Django 4.1.2 on 2023-08-29 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orga", "0006_address_city_address_zipcode_alter_address_country_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Address",),
    ]