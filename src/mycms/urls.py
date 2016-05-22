# -*- coding:utf8 -*-

from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.hello, name='hello'),
    url(r'^a/([0-9]+)/$', views.article, name='article'),
    url(r'^t/(\w+)/$', views.tag, name='tag'),
    url(r'^q/([0-9]+)/$', views.question, name='question'),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^questions/hottest/$', views.questions_hottest, name='questions_hottest'),
    url(r'^questions/unanswered/$', views.questions_unanswered, name='questions_unanswered'),
    url(r'^blogs/$', views.blogs, name='blogs'),
    url(r'^u/(\w+)/$', views.user, name='user'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^write/$', views.write, name='write'),
    url(r'^u/draft/$', views.draft, name='draft'),
    url(r'^u/login_register/$', views.login_register, name='login'),

]

# api part

urlpatterns += [

]

