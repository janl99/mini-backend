# Generated by Django 3.1.1 on 2022-02-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20220206_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatarUrl',
            field=models.CharField(max_length=255, verbose_name='用户头像'),
        ),
    ]