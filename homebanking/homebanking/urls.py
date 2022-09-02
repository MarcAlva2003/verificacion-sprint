"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#agregue
from xml.dom.expatbuilder import DOCUMENT_NODE

from django.contrib import admin
from django.urls import path, include
from ITBANK import views as ITBANK_views
from Clientes import views as Cliente_views
from Cuentas import views as Cuentas_views
from login import views as login_views
from prestamos import views as prestamos_views
from tarjetas import views as tarjetas_views
#imports de las apis
from api.views import Clients, ClientBalance, MontoPrestamosDeCliente, MontoPrestamoSucursal, TarjetasCliente, SolicitudPrestamo, RechazarPrestamo, DireccionClienteID, EditarDireccionCliente, ListaSucursales
# from api.views import ClienteLists,ClienteDetails, PrestamoList,UserDetail,UserList,SucursalLists,SucursalDetails,PrestamoDetails,TarjetasDeCliente, MontoPrestamosDeCliente, BalanceDeCuentaDeCliente, MontoPrestamoSucursal, GetClientList



#agregue
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ITBANK_views.home,name = 'home'),
    path('clientes/',Cliente_views.Clientes, name = 'clientes'),
    path('cuentas/',Cuentas_views.Cuentas, name = 'cuentas'),
    path('login/',login_views.login, name = 'login'),
    path('register/',login_views.register, name = 'register'),
    path('prestamos/',include('prestamos.urls')),
    path('tarjetas/',tarjetas_views.tarjetas, name = 'tarjetas'),
    path('inversiones/',ITBANK_views.inversiones, name = 'inversiones'),
    path('perfil/',ITBANK_views.perfil, name = 'perfil'),
    path('sucycajero/',ITBANK_views.sucycajero, name = 'sucycajero'),
    path('terminos/',ITBANK_views.terminos, name = 'terminos'),
    path('accounts/',include('django.contrib.auth.urls')),

    path('api/cliente', Clients.as_view()),
    path('api/cuentas-cliente', ClientBalance.as_view()),
    path('api/prestamos-cliente', MontoPrestamosDeCliente.as_view()),
    path('api/prestamos-sucursal/<int:sucursal_id>', MontoPrestamoSucursal.as_view()),
    path('api/tarjetas-cliente/<int:customer_id>', TarjetasCliente.as_view()),
    path('api/solicitud-prestamo', SolicitudPrestamo.as_view()),
    path('api/rechazar-prestamo/<int:pk>', RechazarPrestamo.as_view()),
    path('api/direccion-cliente/<int:pk>', DireccionClienteID.as_view()),
    path('api/direccion-cliente', EditarDireccionCliente.as_view()),
    path('api/sucursales',ListaSucursales.as_view()),
    # path('testapi/users/', UserList.as_view()),
    # path('testapi/users/<int:pk>/', UserDetail.as_view()),
    # path('testapi/sucursales/',SucursalLists.as_view()),
    # path('testapi/sucursales/<int:pk>/',SucursalDetails.as_view()),
    # path('testapi/prestamopost/', PrestamoList.as_view()),
    # path('testapi/prestamodelete/<int:pk>',PrestamoDetails.as_view()),
    # path('testapi/montos-prestamo-cliente/<int:customer_id>',MontoPrestamosDeCliente.as_view()),
    # path('testapi/balance-cliente/', BalanceDeCuentaDeCliente.as_view()),
    # path('testapi/monto-prestamo-sucursal/<int:sucursal_id>', MontoPrestamoSucursal.as_view()),
]

#agregue
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,DOCUMENT_root=settings.MEDIA_ROOT)