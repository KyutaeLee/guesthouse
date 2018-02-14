from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hi, name='hi'),
    url(r'^home/', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
]
