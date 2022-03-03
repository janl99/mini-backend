# Generated by Django 3.1.1 on 2022-03-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_addedreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='update_time',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.JSONField(null=True, verbose_name='邮寄地址'),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.FloatField(default=0.0, verbose_name='优惠'),
        ),
        migrations.AddField(
            model_name='order',
            name='netCost',
            field=models.FloatField(default=0.0, verbose_name='实付'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_time',
            field=models.DateTimeField(null=True, verbose_name='支付时间'),
        ),
    ]