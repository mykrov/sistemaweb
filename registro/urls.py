from django.conf.urls import url
from . import views

urlpatterns = [
	
	url(r'^$', views.inicio, name='inicio'),
	url(r'^$', views.manuel, name='manuel'),
	url(r'^$', views.consulta, name='consulta'),
	url(r'^$', views.estadistica, name='estadistica'),

	
]