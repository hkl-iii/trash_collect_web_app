# Generated by Django 3.2.5 on 2021-07-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickup',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
