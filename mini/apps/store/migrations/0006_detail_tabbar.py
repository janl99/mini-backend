# Generated by Django 3.1.1 on 2021-10-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_detail_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='tabbar',
            field=models.JSONField(default=2, verbose_name='导航'),
            preserve_default=False,
        ),
    ]
