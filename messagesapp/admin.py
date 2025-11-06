from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject','sender','receiver','created_at','read')
    list_filter = ('read',)
    search_fields = ('subject','body','sender__username','receiver__username')