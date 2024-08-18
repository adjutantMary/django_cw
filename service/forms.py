from django import forms 

from .models import *


class ClientForm(forms.ModelForm):
    '''Форма записи клиента сервиса'''
    def __init__(self, *args, **kwargs):
        #тут надо добавить настройку пользователя после создания модели User
        user = kwargs.pop('user', None)
        super(ClientForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Client
        fields = ["email", "name", "comment"]
        labels = {
            'email': 'E-mail',
            'name': 'Ваше имя',
            'comment': 'Комментарий',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }
        
        
class MailingForm(forms.ModelForm):
    '''Форма настройки рассылки'''
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        user = None
        if self.request:
            user = self.request.user
        super().__init__(*args, **kwargs)
        #добавить фильтрацию по is_superuser
        
    class Meta:
        model = MailingSettings
        fields = ['name', 'clients', 'start_time', 'period', 'status', 'message']
        labels = {
            'name': 'Название расслыки',
            'clients': 'Клиенты',
            'start_time': 'Время отправки',
            'period': 'Тип рассылки',
            'status': 'Статус',
            'message': 'Сообщение',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'clients': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control'}),
            'period': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Select(attrs={'class': 'form-control'}),
        }
        
    
class MessageForm(forms.ModelForm):
    '''Форма заполнения сообщения для рассылки'''
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MessageForm, self).__init__(*args, **kwargs)
        #и туть надо обработку прав доступа добавить
        
    class Meta:
        model = Message
        fields = ['subject', 'body']
        labels = {
            'subject': 'Тема письма',
            'body': 'Содержание письма',
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        }
        
        