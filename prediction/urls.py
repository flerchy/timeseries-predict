from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<filename>[\w,\s-]+\.csv)/res/$', views.result, name='result'),
    url(r'^(?P<filename>[\w,\s-]+\.[^(csv)]*)/res/$', views.custom404, name='err'),
    url(r'^about/$', views.about, name='about'),
    url(r'^instruction/$', views.instruction, name='instruction'),
]