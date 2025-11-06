from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.PageListView.as_view(), name='list'),               # pages/
    path('create/', views.PageCreateView.as_view(), name='create'),    # crear
    path('<int:pk>/', views.PageDetailView.as_view(), name='detail'),  # leer más
    path('<int:pk>/update/', views.PageUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PageDeleteView.as_view(), name='delete'),
]