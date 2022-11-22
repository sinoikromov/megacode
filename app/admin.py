from django.contrib import admin
from .models import Client


# class ClientAdmin(admin.ModelAdmin):
#     # list_display = ['id', 'first_name', 'second_name', 'is_active', 'status_document']


admin.site.register(Client)
