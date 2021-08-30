# Generated by Django 3.2.6 on 2021-08-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apigw', '0004_auto_20210827_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiservice',
            name='aws_access_key',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='aws_host',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='aws_region',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='aws_secret_access_key',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='aws_service',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='aws_token',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
    ]
