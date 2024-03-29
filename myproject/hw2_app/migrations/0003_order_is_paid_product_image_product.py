# Generated by Django 5.0.2 on 2024-02-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw2_app', '0002_remove_order_product_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='image_product',
            field=models.ImageField(default='No image', upload_to='images/'),
        ),
    ]
