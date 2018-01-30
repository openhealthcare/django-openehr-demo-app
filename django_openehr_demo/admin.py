from django.contrib import admin
import django_openehr.models as ehrmodels

admin.site.register(ehrmodels.AddressDetails)
admin.site.register(ehrmodels.TelecomDetails)
admin.site.register(ehrmodels.Demographics)
admin.site.register(ehrmodels.SymptomSign)
admin.site.register(ehrmodels.TherapeuticDirection)
