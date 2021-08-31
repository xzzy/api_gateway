# Generated by Django 3.2.6 on 2021-08-31 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apigw', '0011_auto_20210831_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiservice',
            name='notes',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='allowed_ips',
            field=models.TextField(blank=True, default='', help_text='Use network ranges format: eg 1 ip = 10.1.1.1/32 or for a c class block of ips use 192.168.1.0/24 etc. Each range should be on it own line.', null=True),
        ),
    ]