from django.forms import formset_factory
from django.shortcuts import render

from django_openehr_demo.forms import (
    RelevantContactForm, AdmissionForm, AllergiesForm
)


def transfer_care(request):

    RelevantContactFormset = formset_factory(RelevantContactForm)
    AdmissionFormset = formset_factory(AdmissionForm)
    AllergiesFormset = formset_factory(AllergiesForm, extra=2)

    if request.method == 'POST':
        relevant_contact_formset = RelevantContactFormset(request.POST, request.FILES, prefix='relevantcontacts')
        admission_formset = AdmissionFormset(request.POST, request.FILES, prefix='admissions')
        allergies_formset = AllergiesFormset(request.POST, request.FILES, prefix='allergies')
        if False: # iterate through all calling .is_valid()
            # Save tehm
            pass
    else:
        relevant_contact_formset = RelevantContactFormset(prefix='relevantcontacts')
        admission_formset = AdmissionFormset(prefix='admissions')
        allergies_formset = AllergiesFormset(prefix='allergies')

    return render(request, 'transfer_care.html', {
        'relevant_contact_formset': relevant_contact_formset,
        'admission_formset': admission_formset,
        'allergies_formset': allergies_formset
    })
