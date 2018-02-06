from django.forms import formset_factory
from django.shortcuts import render

from django_openehr_demo.forms import (
    DemographicProfessionalForm,
    RelevantContactForm,
    AdmissionForm,
    ReasonForEncounterForm,
    AllergiesForm,
)


def transfer_care(request):

    DemographicProfessionalFormset = formset_factory(DemographicProfessionalForm)
    RelevantContactFormset = formset_factory(RelevantContactForm)
    AdmissionFormset = formset_factory(AdmissionForm)
    ReasonForEncounterFormSet = formset_factory(ReasonForEncounterForm)
    AllergiesFormset = formset_factory(AllergiesForm)

    if request.method == 'POST':
        demographic_professional_formset = DemographicProfessionalFormset(request.POST, request.FILES, prefix='demographicprofessional')
        relevant_contact_formset = RelevantContactFormset(request.POST, request.FILES, prefix='relevantcontacts')
        admission_formset = AdmissionFormset(request.POST, request.FILES, prefix='admissions')
        reason_for_encounter_formset = ReasonForEncounterFormSet(request.POST, request.FILES, prefix='reasonforencounter')
        allergies_formset = AllergiesFormset(request.POST, request.FILES, prefix='allergies')
        if False: # iterate through all calling .is_valid()
            # Save them
            pass
    else:
        demographic_professional_formset = DemographicProfessionalFormset(prefix='demographicprofessional')
        relevant_contact_formset = RelevantContactFormset(prefix='relevantcontacts')
        admission_formset = AdmissionFormset(prefix='admissions')
        reason_for_encounter_formset = ReasonForEncounterFormSet(prefix='reasonforencounter')
        allergies_formset = AllergiesFormset(prefix='allergies')

    return render(request, 'transfer_care.html', {
        'demographic_professional_formset': demographic_professional_formset,
        'relevant_contact_formset': relevant_contact_formset,
        'admission_formset': admission_formset,
        'reason_for_encounter_formset': reason_for_encounter_formset,
        'allergies_formset': allergies_formset
    })
