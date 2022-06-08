from django.urls import path
from cliente import views, views_dispositivo


urlpatterns = [
    path('', views_dispositivo.BienvenidaView.as_view(), name='bienvenida'),
    
    path('cliente/', views.lista_clientes, name='cliente_lista'),
    path('cliente/nuevo', views.nuevo_cliente, name='nuevo_cliente'),
    path('cliente/eliminar/<int:id>', views.eliminar_cliente, name='eliminar_cliente'),
    path('cliente/editar/<int:id>', views.editar_cliente, name='editar_cliente'),

    path('dispositivo/', views_dispositivo.ListaDispositivo.as_view(), name='dispositivo_lista'),
    path('dispositivo/nuevo', views_dispositivo.NuevoDispositivoView.as_view(), name='nuevo_dispositivo'),
    path('dispositivo/editar/<int:pk>', views_dispositivo.EditarDispositivoView.as_view(), name='editar_dispositivo'),
    path('dispositivo/eliminar/<int:pk>', views_dispositivo.EliminarDispositivoView.as_view(), name='eliminar_dispositivo'),

]
