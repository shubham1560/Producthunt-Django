# Generated by Django 2.2.2 on 2019-09-17 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20190917_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfeedback',
            name='parComment',
            field=models.ForeignKey(default=3083200227470499, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductFeedback'),
        ),
    ]