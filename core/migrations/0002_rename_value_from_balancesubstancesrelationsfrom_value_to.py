# Generated by Django 4.2.7 on 2023-12-06 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balancesubstancesrelationsfrom',
            old_name='value_from',
            new_name='value_to',
        ),
    ]