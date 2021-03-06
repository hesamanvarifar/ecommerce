# Generated by Django 4.0.4 on 2022-06-10 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customer_options_alter_supplier_options_and_more'),
        ('cart_shipment', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='delivery_address_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='user.customeraddress'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='delivery_type_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='cart_shipment.deliverytype'),
        ),
    ]
