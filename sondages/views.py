from django.http import HttpResponse
from django.shortcuts import render
from .models import Service, About_models, contact


def index(request,):
    services = Service.objects.all()
    data = {'services': services}
    return render(request, 'index.html', data)

def about(request):
    abouts = About_models.objects.all()
    data = {'abouts': abouts}
    return render(request, 'about.html', data)

def contact_list(request):
    relation  = contact.objects.all()
    data  = {'relation': relation}
    return render(request, 'contact.html', data)

def service_list(request):
    services = Service.objects.all()
    data = {'services': services}
    return render(request, 'service.html', data)

def about_view(request):
    abouts = About_models.objects.all()
    data = {'abouts': abouts}
    return render(request, 'index.html', data)
