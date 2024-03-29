# Generated by Django 3.1.1 on 2021-09-18 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='名称')),
                ('totalRead', models.IntegerField(verbose_name='阅读量')),
                ('totalLike', models.IntegerField(verbose_name='点赞数')),
                ('review', models.IntegerField(verbose_name='评论数')),
                ('author', models.CharField(max_length=10, verbose_name='作者')),
                ('caption', models.CharField(max_length=100, verbose_name='插图')),
                ('profile', models.CharField(max_length=100, verbose_name='肖像')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('groupList', models.CharField(max_length=80, verbose_name='分组列表')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('select', models.BooleanField(default=False, null=True, verbose_name='勾选')),
                ('top', models.BooleanField(default=False, null=True, verbose_name='勾选')),
                ('conceal', models.BooleanField(default=False, null=True, verbose_name='勾选')),
            ],
            options={
                'verbose_name': '文章详情',
                'verbose_name_plural': '文章详情',
                'db_table': 'tb_article',
            },
        ),
        migrations.CreateModel(
            name='ArticleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.JSONField(verbose_name='文章分组')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '文章分组',
                'verbose_name_plural': '文章分组',
                'db_table': 'tb_article_group',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=100, verbose_name='肖像')),
                ('author', models.CharField(max_length=10, verbose_name='作者')),
                ('article', models.IntegerField(default=0, verbose_name='文章数')),
                ('active', models.BooleanField(default=True, verbose_name='激活')),
                ('remark', models.CharField(max_length=100, null=True, verbose_name='标签')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '作者详情',
                'verbose_name_plural': '作者详情',
                'db_table': 'tb_author',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='名称')),
                ('format', models.CharField(max_length=10, verbose_name='格式')),
                ('size', models.CharField(max_length=20, verbose_name='图像尺寸')),
                ('fileSize', models.CharField(max_length=20, verbose_name='图像大小')),
                ('src', models.CharField(max_length=100, verbose_name='链接地址')),
                ('group', models.CharField(max_length=20, verbose_name='分组名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('select', models.BooleanField(default=False, null=True, verbose_name='勾选')),
            ],
            options={
                'verbose_name': '图片详情',
                'verbose_name_plural': '图片详情',
                'db_table': 'tb_image',
                'ordering': ['-update_time', '-create_time', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ImageGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.JSONField(max_length=1000, verbose_name='视频分组')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '图像分组',
                'verbose_name_plural': '图像分组',
                'db_table': 'tb_image_group',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='名称')),
                ('format', models.CharField(max_length=10, verbose_name='格式')),
                ('size', models.CharField(max_length=20, verbose_name='视频尺寸')),
                ('fileSize', models.CharField(max_length=20, verbose_name='视频大小')),
                ('playTime', models.CharField(max_length=10, verbose_name='播放时长')),
                ('src', models.CharField(max_length=100, verbose_name='视频地址')),
                ('url', models.CharField(max_length=100, verbose_name='封面地址')),
                ('textarea', models.CharField(max_length=500, verbose_name='视频简介')),
                ('group', models.CharField(max_length=20, verbose_name='分组名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('select', models.BooleanField(default=False, null=True, verbose_name='勾选')),
            ],
            options={
                'verbose_name': '视频详情',
                'verbose_name_plural': '视频详情',
                'db_table': 'tb_video',
                'ordering': ['-update_time', '-create_time', 'title'],
            },
        ),
        migrations.CreateModel(
            name='VideoGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.JSONField(verbose_name='图片分组')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '视频分组',
                'verbose_name_plural': '视频分组',
                'db_table': 'tb_video_group',
            },
        ),
    ]
