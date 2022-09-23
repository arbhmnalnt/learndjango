from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_clients_api', views.get_clients_api.as_view(), name='get_client_api'),
    path('get_client_services_api/<int:client_id>', views.get_client_services_api, name='get_client_services_api')
]