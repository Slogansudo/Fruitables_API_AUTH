# Generated by Django 5.0.4 on 2024-05-12 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_order_users_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='order_users_count',
            new_name='products_count',
        ),
    ]