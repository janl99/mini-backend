# Generated by Django 3.1.1 on 2022-02-21 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_auto_20220215_1007'),
        ('orders', '0002_auto_20220201_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.FloatField(default=0, verbose_name='总价'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(default='', max_length=125, verbose_name='描述'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', to_field='openid', verbose_name='顾客'),
        ),
    ]
