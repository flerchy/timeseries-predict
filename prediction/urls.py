from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<filename>[\w,\s-]+\.[A-Za-z]{3})/res/$', views.result, name='result')
]