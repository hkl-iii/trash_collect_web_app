# Generated by Django 3.2.5 on 2021-07-11 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_customer_suspended'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='suspended',
            new_name='is_suspended',
        ),
    ]
