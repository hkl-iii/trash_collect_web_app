# Generated by Django 3.1.8 on 2021-05-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20210512_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pickup_date',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
