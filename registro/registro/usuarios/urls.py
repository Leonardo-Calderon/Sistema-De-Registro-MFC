from django.urls import path
# from articulos import views, views_categoria
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'
# usuarios:logout
# usuarios:perfil

urlpatterns = [
    path('salir', LogoutView.as_view(), name='logout'),
    path('entrar', views.LoginView.as_view(), name='login'),
    path('registrar', views.RegistrarView.as_view(), name='registrar'),
    path('perfil', views.CrearPerfilView.as_view(), name='perfil'),
    path('lista', views.ListaUsuariosView.as_view(), name='lista'),
    path('grupos', views.asignar_grupos, name='asignar_grupos'),
    path('activar/<slug:uidb64>/<slug:token>', views.ActivarCuentaView.as_view(), name='activar'),
]
