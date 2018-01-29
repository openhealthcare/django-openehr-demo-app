from django.contrib import admin
from django_openehr import models

admin.site.register(models.AddressDetails)
admin.site.register(models.TelecomDetails)
admin.site.register(models.Demographics)
admin.site.register(models.SymptomSign)
admin.site.register(models.TherapeuticDirection)
