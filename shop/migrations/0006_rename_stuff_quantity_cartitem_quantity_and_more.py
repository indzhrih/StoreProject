# Generated by Django 5.1.4 on 2024-12-15 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_cart_quantity_remove_cart_total_cart_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='stuff_quantity',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.cart'),
        ),
    ]
