from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.ver_curso, name='ver_curso'),
    path('agregar/', views.agregar_curso, name='agregar_curso'),
    path('editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('eliminar/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
]
