# Generated by Django 4.0.4 on 2022-05-19 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart_shipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cart_shipment.order')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTypeDataKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_name', models.CharField(max_length=50)),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='payment.paymenttype')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecordDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_detail_value', models.CharField(max_length=100)),
                ('record_detail_key', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='payment.paymenttypedatakey')),
                ('record_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.paymentrecord')),
            ],
        ),
        migrations.AddField(
            model_name='paymentrecord',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='payment.paymenttype'),
        ),
    ]
