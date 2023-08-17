from django.urls import path, include
from .views import *
from .models import *
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', index, name="inicio" ),
    path('nuevos/', NuevosList.as_view(), name='nuevos'),
    path('usados/', UsadosList.as_view(), name='usados'),
    path('service/', ServiceList.as_view(), name='service'),
    path('administracion/', AdministracionList.as_view(), name='administracion'),
#-------------------------
    path('create_usado/', UsadosCreate.as_view(), name='create_usado'),
    path('create_nuevo/', NuevosCreate.as_view(), name='create_nuevo'),
    path('create_service/', ServiceCreate.as_view(), name='create_service'),
    path('create_administracion/', AdministracionCreate.as_view(), name='create_administracion'),
#-------------------------
    path('detail_service/<int:pk>/', ServiceDetail.as_view(), name='detail_service'),
    path('detail_nuevos/<int:pk>/', NuevosDetail.as_view(), name='detail_nuevos'),
    path('detail_usados/<int:pk>/', UsadosDetail.as_view(), name='detail_usados'),
    path('detail_administracion/<int:pk>/', AdministracionDetail.as_view(), name='detail_administracion'),
#-------------------------
    path('update_usado/<int:pk>/', UsadosUpdate.as_view(), name='update_usado'),
    path('update_nuevo/<int:pk>/', NuevosUpdate.as_view(), name='update_nuevo'),
    path('update_service/<int:pk>/', ServiceUpdate.as_view(), name='update_service'),
    path('update_administracion/<int:pk>/', AdministracionUpdate.as_view(), name='update_administracion'),
#-------------------------
    path('delete_usado/<int:pk>/', UsadosDelete.as_view(), name='delete_usado'),
    path('delete_nuevo/<int:pk>/', NuevosDelete.as_view(), name='delete_nuevo'),
    path('delete_service/<int:pk>/', ServiceDelete.as_view(), name='delete_service'),
    path('delete_administracion/<int:pk>/', AdministracionDelete.as_view(), name='delete_administracion'),
#-------------------------
    path('login', login_request, name='login'),
    path('logout', LogoutView.as_view(template_name="aplicacion/logout.html"), name='logout'),
    path('register/', register, name='register'),


]
