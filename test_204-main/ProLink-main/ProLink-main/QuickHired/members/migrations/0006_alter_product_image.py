# Generated by Django 3.2.12 on 2023-05-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_rename_cart_panier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products_images/'),
        ),
    ]