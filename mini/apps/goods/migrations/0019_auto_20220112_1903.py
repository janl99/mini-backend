# Generated by Django 3.1.1 on 2022-01-12 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0018_auto_20220112_1902'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='GoodsReview',
        ),
        migrations.AlterModelOptions(
            name='goodsreview',
            options={'ordering': ['-star'], 'verbose_name': 'tb_goods_review', 'verbose_name_plural': 'tb_goods_review'},
        ),
        migrations.AlterModelTable(
            name='goodsreview',
            table='tb_goods_review',
        ),
    ]
