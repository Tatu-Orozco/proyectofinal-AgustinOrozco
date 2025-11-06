from django.urls import path
from .views import inbox, message_detail, message_create

app_name = 'messages'

urlpatterns = [
    path('', inbox, name='inbox'),
    path('create/', message_create, name='create'),
    path('<int:pk>/', message_detail, name='detail'),
]