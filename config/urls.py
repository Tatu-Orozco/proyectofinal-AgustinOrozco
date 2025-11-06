from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),          # Home y About
    path('pages/', include('pages.urls')),   # Listado y CRUD
    path('accounts/', include('accounts.urls')),  # login/signup/profile
    path('messages/', include('messagesapp.urls')), # mensajería
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)