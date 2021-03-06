# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 18:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('memo', models.CharField(blank=True, max_length=1000)),
                ('title', models.CharField(max_length=120)),
                ('content', models.CharField(blank=True, max_length=20000)),
                ('article_type', models.SmallIntegerField(choices=[(0, '\u6587\u7ae0'), (1, '\u95ee\u9898'), (2, '\u56de\u7b54')], default=0)),
                ('status', models.SmallIntegerField(choices=[(0, '\u8349\u7a3f'), (1, '\u53d1\u8868'), (2, '\u91c7\u7eb3'), (3, '\u5220\u9664'), (4, '\u52a0\u7cbe')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('memo', models.CharField(blank=True, max_length=1000)),
                ('rating', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('favorite', models.IntegerField(default=0)),
                ('read', models.IntegerField(default=0)),
                ('subscribe', models.IntegerField(default=0)),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mycms.Article')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleStatisticDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('memo', models.CharField(blank=True, max_length=1000)),
                ('statistic_type', models.SmallIntegerField(choices=[(0, '\u9605\u8bfb'), (1, '\u559c\u6b22'), (2, '\u8ba8\u538c'), (3, '\u6536\u85cf'), (4, '\u8ba2\u9605')], default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycms.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ATag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('memo', models.CharField(blank=True, max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=200)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtag_set', to='mycms.ATag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('memo', models.CharField(blank=True, max_length=1000)),
                ('content', models.CharField(max_length=1000)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycms.Article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserATagStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('memo', models.CharField(blank=True, max_length=1000)),
                ('article_count', models.IntegerField(default=0)),
                ('elite_article_count', models.IntegerField(default=0)),
                ('atag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_statics', to='mycms.ATag')),
                ('p_atag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_statics_parent', to='mycms.ATag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserBrowseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('memo', models.CharField(blank=True, max_length=1000)),
                ('ua', models.CharField(blank=True, max_length=2000)),
                ('ip', models.CharField(blank=True, max_length=1000)),
                ('url', models.CharField(blank=True, max_length=2000)),
                ('related_user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('memo', models.CharField(blank=True, max_length=1000)),
                ('qq', models.CharField(blank=True, max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('memo', models.CharField(blank=True, max_length=1000)),
                ('credit', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='atag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mycms.ATag'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_set', to='mycms.Article'),
        ),
    ]
