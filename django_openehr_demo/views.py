"""
Views for our Django openEHR demo app
"""
from django.db import transaction
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django_openehr_demo.models import TransferOfCareSummary
from django_openehr import models as ehrmodels
from django.views.generic.detail import DetailView


from django_openehr_demo.forms import (
    AdmissionForm,
    AllergiesForm,
    ClinicalSynopsisForm,
    DemographicProfessionalForm,
    ProblemDiagnosisSummaryForm,
    ProblemsIssuesForm,
    ReasonForEncounterForm,
    RelevantContactForm,
)


def transfer_care(request):

    AdmissionFormset = formset_factory(AdmissionForm)
    AllergiesFormset = formset_factory(AllergiesForm)
    ClinicalSynopsisFormset = formset_factory(ClinicalSynopsisForm)
    DemographicProfessionalFormset = formset_factory(DemographicProfessionalForm)
    ProblemDiagnosisSummaryFormset = formset_factory(ProblemDiagnosisSummaryForm)
    ProblemsIssuesFormset = formset_factory(ProblemsIssuesForm)
    ReasonForEncounterFormSet = formset_factory(ReasonForEncounterForm)
    RelevantContactFormset = formset_factory(RelevantContactForm)

    if request.method == 'POST':
        admission_formset = AdmissionFormset(request.POST, request.FILES, prefix='admissions')
        allergies_formset = AllergiesFormset(request.POST, request.FILES, prefix='allergies')
        clinical_synopsis_formset = ClinicalSynopsisFormset(request.POST, request.FILES, prefix='clinsynopsis')
        demographic_professional_formset = DemographicProfessionalFormset(request.POST, request.FILES, prefix='demoprof')
        problem_diagnosis_formset = ProblemDiagnosisSummaryFormset(request.POST, request.FILES, prefix='probdiag')
        problems_issues_formset = ProblemsIssuesFormset(request.POST, request.FILES, prefix='probissue')
        relevant_contact_formset = RelevantContactFormset(request.POST, request.FILES, prefix='relevantcontacts')
        reason_for_encounter_formset = ReasonForEncounterFormSet(request.POST, request.FILES, prefix='reasonforenc')

        formset_dict = {
            'admission': admission_formset,
            'allergies': allergies_formset,
            'clinical_synopsis': clinical_synopsis_formset,
            'demographic_professional': demographic_professional_formset,
            'diagnoses': problem_diagnosis_formset,
            # problems_issues_formset,
            'reason_for_encounter': reason_for_encounter_formset,
            'relevant_contact': relevant_contact_formset,
        }

        if validate_formsets(formset_dict):
            with transaction.atomic():
                transfer_of_care = TransferOfCareSummary()
                save_all_the_formsets(formset_dict, transfer_of_care)
                transfer_of_care.save()
                return redirect(transfer_of_care.get_absolute_url())
        else:
            pass # Something is invalid. If we just let the call to
        # render() below handle this, it will take the POSTed data
        # and display it in the form along with any error messages.

    else:
        admission_formset = AdmissionFormset(prefix='admissions')
        allergies_formset = AllergiesFormset(prefix='allergies')
        clinical_synopsis_formset = ClinicalSynopsisFormset(prefix='clinsynopsis')
        demographic_professional_formset = DemographicProfessionalFormset(prefix='demoprof')
        problem_diagnosis_formset = ProblemDiagnosisSummaryFormset(prefix='probdiag')
        problems_issues_formset = ProblemsIssuesFormset(prefix='probissue')
        reason_for_encounter_formset = ReasonForEncounterFormSet(prefix='reasonforenc')
        relevant_contact_formset = RelevantContactFormset(prefix='relevantcontacts')

    return render(request, 'transfer_care.html', {
        'admission_formset': admission_formset,
        'allergies_formset': allergies_formset,
        'clinical_synopsis_formset': clinical_synopsis_formset,
        'demographic_professional_formset': demographic_professional_formset,
        'problem_diagnosis_formset': problem_diagnosis_formset,
        'problems_issues_formset': problems_issues_formset,
        'reason_for_encounter_formset': reason_for_encounter_formset,
        'relevant_contact_formset': relevant_contact_formset,
    })


def validate_formsets(formset_dict):
    formsets_are_all_valid = True
    for formset_name, formset_object in formset_dict.items():
        if formset_object.is_valid():
            pass
        else:
            formsets_are_all_valid = False
    return formsets_are_all_valid


def save_all_the_formsets(formset_dict, transfer_of_care):
    for formset_name, formset_object in formset_dict.items():
        for form in formset_object:
            setattr(transfer_of_care, formset_name, form.save())


class TransferOfCareSummaryView(DetailView):
    model = TransferOfCareSummary
