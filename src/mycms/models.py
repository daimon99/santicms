# coding=utf-8
# -*- coding:utf8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.

class MyBaseModel(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    memo = models.CharField(max_length=1000, blank=True)

    class Meta:
        abstract = True


class ATag(MyBaseModel):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subtag_set', blank=True, null=True)


class Article(MyBaseModel):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=20000, blank=True)
    atag = models.ForeignKey(ATag, on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    article_type = models.SmallIntegerField(choices=[(0, u'文章'), (1, u'问题'), (2, u'回答')], default=0)
    parent = models.ForeignKey('self', related_name='answer_set', blank=True, null=True)
    status = models.SmallIntegerField(choices=[(0, u'草稿'), (1, u'发表'), (2, u'采纳'), (3, u'删除'), (4, u'加精')])


class ArticleStatistic(MyBaseModel):
    article = models.OneToOneField(Article)
    rating = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    favorite = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    subscribe = models.IntegerField(default=0)


class ArticleStatisticDetail(MyBaseModel):
    article = models.ForeignKey(Article)
    user = models.ForeignKey(auth_models.User)
    statistic_type = models.SmallIntegerField(default=0,
                                              choices=[(0, '阅读'), (1, '喜欢'), (2, '讨厌'), (3, '收藏'), (4, '订阅')])


class Reply(MyBaseModel):
    article = models.ForeignKey(Article)
    author = models.ForeignKey(auth_models.User)
    content = models.CharField(max_length=1000)


class UserStatistics(MyBaseModel):
    user = models.OneToOneField(auth_models.User)
    credit = models.IntegerField(default=0)


class UserATagStatistics(MyBaseModel):
    user = models.ForeignKey(auth_models.User)
    atag = models.ForeignKey(ATag, related_name='user_statics')
    p_atag = models.ForeignKey(ATag, related_name='user_statics_parent')
    article_count = models.IntegerField(default=0)
    elite_article_count = models.IntegerField(default=0)


class UserProfile(MyBaseModel):
    user = models.ForeignKey(auth_models.User)
    qq = models.CharField(max_length=20, blank=True)


class UserBrowseHistory(MyBaseModel):
    user = models.ForeignKey(auth_models.User)
    ua = models.CharField(max_length=2000, blank=True)
    ip = models.CharField(max_length=1000, blank=True)
    url = models.CharField(max_length=2000, blank=True)
    related_user = models.ForeignKey(auth_models.User, blank=True, null=True, related_name='related_user')


def get_blogs_recommended(page=1):
    per_page = 10
    start = 10 * (page - 1)
    end = 10 * page
    max_content = 100
    articles = Article.objects.values('title', 'content', 'articlestatistic__rating', 'articlestatistic__read',
                                      'articlestatistic__subscribe', 'author__username', 'create_time',
                                      'atag__name').filter(article_type=0).order_by('-create_time')[start:end]
    blogs = [dict(rating=a['articlestatistic__rating'] if a['articlestatistic__rating'] else 0,
                  reading=a['articlestatistic__read'] if a['articlestatistic__read'] else 0,
                  title=a['title'],
                  content_short=a['content'][:max_content],
                  author=a['author__username'],
                  atag=a['atag__name'],
                  create_time=a['create_time'],
                  favorites=a['articlestatistic__subscribe'] if a['articlestatistic__subscribe'] else 0,
                  ) for a in articles]
    return blogs
