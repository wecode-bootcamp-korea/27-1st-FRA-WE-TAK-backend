# Generated by Django 3.2.9 on 2021-12-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.URLField(max_length=500),
        ),
    ]