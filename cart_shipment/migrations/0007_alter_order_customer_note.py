# Generated by Django 4.0.4 on 2022-06-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_shipment', '0006_alter_cartitem_product_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_note',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
