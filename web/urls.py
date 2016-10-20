"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from registro.views import inicio, historia,manuel,consulta, buscar_paciente


#from registro import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('smart_selects.urls')),
    url(r'^inicio/$',inicio),
    url(r'^historia/',historia),
    url(r'^manuel/',manuel),
    url(r'^consulta/',consulta),
    #el  parametro de la URL debe coincidir con el parametro de la vista, en este caso es 'ci'
    url(r'^buscar/(?P<ci>\d+)/',buscar_paciente, name='busqueda_paciente'),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	               