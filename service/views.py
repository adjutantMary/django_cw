from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


@login_required
def client_list(request):
    '''Отображение всех клиентов'''
    clients = Client.objects.all()
    return render(request, 'mailing_service/client_list.html', {'client': clients})

@login_required
def client_detail_list(request, pk):
    '''Отображение детальной информации по клиенту'''
    client = Client.objects.get(pk=pk)
    return render(request, 'mailing_service/client_detail.html', {'client': client})

@login_required
def create_client(request):
    '''Создание клиента'''
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.owner = request.user
            client.save()
            return redirect('mailing:client_list')
        
    else:
        form = ClientForm()
    return render(request, 'mailing_service/client_form.html', {'form': form})

@login_required
def update_client(request, pk):
    '''Обновление информации о клиенте'''
    client = Client.objects.get(pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('mailing:client_list')
        
    else:
        form = ClientForm(instance=client)
    return render(request, 'mailing_service/client_form.html', {'form': form})
