from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_list, name="contact"),
    path("service_list/", views.service_list, name="service"),
    path(' about_view', views. about_view, name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)