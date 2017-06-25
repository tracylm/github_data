from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tracy/$', views.tracy, name='tracy'),
    url(r'^success/$', views.success, name='success'),
]
