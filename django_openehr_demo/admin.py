from django.contrib import admin
import django_openehr.models as ehrmodels

admin.site.register(ehrmodels.AddressDetails)
admin.site.register(ehrmodels.AdverseReaction)
admin.site.register(ehrmodels.DemographicPersonal)
admin.site.register(ehrmodels.DemographicProfessional)
admin.site.register(ehrmodels.Identifier)
admin.site.register(ehrmodels.InpatientAdmission)
admin.site.register(ehrmodels.PersonName)
admin.site.register(ehrmodels.ProblemDiagnosis)
admin.site.register(ehrmodels.ReasonForEncounter)
admin.site.register(ehrmodels.RelevantContact)
admin.site.register(ehrmodels.SymptomSign)
admin.site.register(ehrmodels.TelecomDetails)
admin.site.register(ehrmodels.TherapeuticDirection)
