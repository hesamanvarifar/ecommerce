# Generated by Django 4.0.4 on 2022-06-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_comment_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.PositiveSmallIntegerField(),
        ),
    ]