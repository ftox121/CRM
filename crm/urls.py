from django.urls import path
from crm.views import *
app_name = 'crm'

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('settings/', settings, name='settings'),
    path('dashboard/', orders_view, name='dashboard'),
    path('delete/<int:order_id>', delete_order, name='delete_order'),
    path('clients/', clients_view, name='clients'),
    path('clients/delete/<int:client_id>/', delete_client, name='delete_client'),
    path('clients/edit/<int:client_id>/', edit_client, name='edit_client'),
]