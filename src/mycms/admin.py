# -*- coding:utf8 -*-

from django.contrib import admin
import models as m

# Register your models here.


@admin.register(m.Article, m.ArticleStatistic, m.ArticleStatisticDetail, m.ATag, m.Reply, m.UserATagStatistics,
               m.UserBrowseHistory,
               m.UserProfile, m.UserStatistics)
class CommonAdmin(admin.ModelAdmin):
    pass
