from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='reviewapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', views.registro_view, name='register'), 
    path('contenido/', views.lista_contenido, name='contenido_lista'),
    path('contenido/<int:pk>/', views.contenido_detail, name='detalle_contenido'),
]