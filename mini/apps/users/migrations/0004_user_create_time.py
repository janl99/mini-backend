# Generated by Django 3.1.1 on 2021-11-04 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211104_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='注册时间'),
        ),
    ]