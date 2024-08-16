from django.contrib import admin
from .models import *


class MyAdminSite(admin.AdminSite):
    site_header = "Информация о рассылках"

mail_admin = MyAdminSite(name="mail-admin")


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment',]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'body',]
    
@admin.register(MailingSettings)
class MailingAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'end_time', 'period', 'status', 'message',]
    date_hierarchy = 'start_time'
    
@admin.register(Attempt)
class AttemtAdmin(admin.ModelAdmin):
    list_display = ['mailing_settings', 'created_at', 
                    'is_success', 'details',]
    date_hierarchy = 'created_at'
    
mail_admin.register(Message, MessageAdmin)
mail_admin.register(Client, ClientAdmin)
mail_admin.register(MailingSettings, MailingAdmin)
mail_admin.register(Attempt, AttemtAdmin)
    