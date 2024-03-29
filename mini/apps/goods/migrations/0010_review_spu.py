# Generated by Django 3.1.1 on 2022-01-09 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20211223_1848'),
        ('goods', '0009_auto_20211230_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='SPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defaultImageUrl', models.CharField(max_length=100, null=True, verbose_name='商品图片')),
                ('reviews', models.IntegerField(null=True, verbose_name='评论数')),
                ('sales', models.IntegerField(null=True, verbose_name='销量')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_spus', to='store.store', verbose_name='店铺')),
            ],
            options={
                'verbose_name': 'spu',
                'verbose_name_plural': 'spu',
                'db_table': 'tb_spu',
                'ordering': ['-sales'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField(default=5, verbose_name='星数')),
                ('likes', models.IntegerField(default=0, verbose_name='点赞量')),
                ('reviews', models.IntegerField(default=0, verbose_name='评论数')),
                ('children', models.JSONField(null=True, verbose_name='子评论')),
                ('name', models.CharField(max_length=50, verbose_name='用户名')),
                ('msg', models.CharField(max_length=250, verbose_name='评论')),
                ('avatar', models.CharField(max_length=100, verbose_name='用户头像')),
                ('imgs', models.JSONField(null=True, verbose_name='评论图片')),
                ('additional', models.JSONField(null=True, verbose_name='追加评论')),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_reviews', to='goods.spu', verbose_name='评论')),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'review',
                'db_table': 'tb_review',
                'ordering': ['-star'],
            },
        ),
    ]
