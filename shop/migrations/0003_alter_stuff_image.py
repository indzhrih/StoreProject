# Generated by Django 5.1.4 on 2024-12-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_stuff_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
