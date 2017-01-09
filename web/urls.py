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
from registro.views import inicio, mapa, addenf, std, buscar_paciente, manuel, consulta, estadistica1, estadistica2
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

#from registro import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^manuel/',login_required(manuel),name='manuel'),
    url(r'^consulta/',login_required(consulta),name='consulta'),
    #el  parametro de la URL debe coincidir con el parametro de la vista, en este caso es 'ci'
    #url(r'^buscar/(?P<ci>\d+)/',buscar_paciente, name='busqueda_paciente'),
    url(r'^buscar/',login_required(buscar_paciente), name='busqueda_paciente'),
    url(r'^estadisticas/',login_required(estadistica1), name='estadisticas'),
    url(r'^estadisticas2/',login_required(estadistica2), name='estadisticas2'),
    url(r'accounts/login/',login,{'template_name':'login.html'},name='login'),
    url(r'^logout/',logout_then_login,name='logout'),
    url(r'^mapa/',login_required(mapa),name='mapa'),
    url(r'^std/',login_required(std),name='std'),
    url(r'^addenf/',addenf,name='addenf'),
] 
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	               