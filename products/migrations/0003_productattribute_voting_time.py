# Generated by Django 2.2.2 on 2019-09-15 08:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productattribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='voting_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
