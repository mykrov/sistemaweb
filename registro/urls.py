from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.registrop, name='registrop'),
	url(r'^$', views.inicio, name='inicio'),
	
]