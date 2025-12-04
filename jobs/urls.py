from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('nova-vaga', views.job_create, name='job_create'),# Rota para criar uma nova vaga
    path('editar/<int:id>/', views.job_edit, name='job_edit'),# Rota para editar uma vaga existente
    path('apagar/<int:id>/', views.job_delete, name='job_delete'),# Rota para apagar uma vaga existente
]