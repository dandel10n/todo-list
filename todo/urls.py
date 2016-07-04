from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'^task/(?P<pk>\d+)/$', views.task_info, name='task_info'),
    url(r'^task/new/$', views.new_task, name='new_task'),
    url(r'^task/(?P<pk>\d+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^task/(?P<pk>\d+)/remove/$', views.task_remove, name='task_remove'),
]
