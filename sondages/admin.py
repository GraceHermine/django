from django.contrib import admin
from .models import Service, avis,contact,About_models,rendez_vous

admin.site.register(Service)
admin.site.register(contact)
admin.site.register(About_models)
admin.site.register(rendez_vous)
admin.site.register(avis)
# Register your models here.
