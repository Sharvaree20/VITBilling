# Generated by Django 4.0 on 2021-12-28 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0008_alter_customer_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_price',
        ),
    ]
