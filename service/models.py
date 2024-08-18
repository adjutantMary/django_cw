from django.db import models
from django.utils import timezone

class Client(models.Model):
    '''Клиент сервиса'''
    
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=128, blank=True, null=True)
    comment = models.TextField(max_length=320, blank=True, null=True)
    
    
class Message(models.Model):
    '''Сообщение для рассылки'''
    
    subject = models.CharField(max_length=128, blank=True, null=True)
    body = models.TextField(max_length=320, blank=True, null=True)
    
    
class MailingSettings(models.Model):
    '''Настройки рассылки'''
    
    class Period(models.TextChoices):
        DAILY = 'D', 'Daily'
        WEEKLY = 'W', 'Weekly'
        MONTHLY = 'M', 'Monthly'
    
    class Status(models.TextChoices):
        CREATED = 'C', 'Created'
        LAUNCHED = 'L', 'Launched'
        INACTIVE = 'I', 'Inactive'
        
    start_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    end_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    period = models.CharField(choices=Period.choices, default=Period.WEEKLY, max_length=2)
    date_start = models.DateField(verbose_name='Дата начала рассылки', default=timezone.now)
    date_next = models.DateTimeField(verbose_name="следующая дата рассылки", default=timezone.now)
    
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.INACTIVE, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Активация рассылки')
    
    clients = models.ManyToManyField(Client)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    
    last_sent_time = models.DateTimeField(null=True, blank=True)
 
    
class Attempt(models.Model):
    '''Попытка рассылки'''
    
    mailing_settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_success = models.BooleanField(default=False)
    details = models.TextField(null=True, blank=True)
    