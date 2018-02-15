from django.db import models
from django_openehr import models as ehrmodels
from django.shortcuts import reverse


class TransferOfCareSummary(models.Model):

    demographic_professional = models.ForeignKey(
        ehrmodels.DemographicProfessional,
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

    relevant_contact = models.ForeignKey(
        ehrmodels.RelevantContact,
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

    admission = models.ForeignKey(
        ehrmodels.InpatientAdmission,
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

    reason_for_encounter = models.ForeignKey(
        ehrmodels.ReasonForEncounter,
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

    allergies = models.ForeignKey(
        ehrmodels.AdverseReaction,
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

    diagnoses = models.ForeignKey(
        ehrmodels.ProblemDiagnosis,
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

#    problems_issues = models.ForeignKey(
#        ehrmodels.ProblemDiagnosis,
#        blank=True, null=True,
#        on_delete=models.SET_NULL,
#    )

    clinical_synopsis = models.ForeignKey(
        ehrmodels.ClinicalSynopsis,
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

    def get_absolute_url(self):
        return reverse('transfer_of_care_detail', kwargs={'pk': self.id} )
