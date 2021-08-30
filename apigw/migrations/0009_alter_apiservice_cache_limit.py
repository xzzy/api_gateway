# Generated by Django 3.2.6 on 2021-08-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apigw', '0008_auto_20210830_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiservice',
            name='cache_limit',
            field=models.IntegerField(default=60, help_text='Cache expiry limit in seconds'),
        ),
    ]