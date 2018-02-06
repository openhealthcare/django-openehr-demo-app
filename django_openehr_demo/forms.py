# IDCR Transfer of Care summary (minimal)
from django import forms
import django_openehr.models as ehrmodels


# SECTION Relevant contacts [0..*]
# openEHR-EHR-SECTION.relevant_contacts_rcp.v1

class DemographicProfessionalForm(forms.ModelForm):
    # CLUSTER Personal details => openEHR-EHR-CLUSTER.individual_professional_uk.v1
    #   => INCLUDES CLUSTER Person name => openEHR-EHR-CLUSTER.person_name.v1
    # INCLUDES CLUSTER Telecom details => openEHR-EHR-CLUSTER.telecom_uk.v1
    class Meta:
        model = ehrmodels.DemographicProfessional
        fields = [
            'person_name',             # TODO should be ELEMENT Full name FROM PersonName
            'telecom_details',         # ELEMENT Telecoms
            'professional_group'       # ELEMENT Professional group
        ]

class RelevantContactForm(forms.ModelForm):
    # ADMIN_ENTRY Relevant contact [0..*]
    # from openEHR-EHR-ADMIN_ENTRY.relevant_contact_rcp.v0
    class Meta:
        model = ehrmodels.RelevantContact
        fields = [
            'relationship_category',   # ELEMENT Relationship category
            'relationship',            # ELEMENT Relationship
            'is_next_of_kin',          # ELEMENT Is next of kin?
            'relationship_note',       # ELEMENT Note
            'date_updated'             # ELEMENT Date updated
        ]


# SECTION Admission details [0..*]
# openEHR-EHR-SECTION.admission_details_rcp.v1

class AdmissionForm(forms.ModelForm):
    # ADMIN_ENTRY Inpatient admission [0..*]
    # openEHR-EHR-ADMIN_ENTRY.inpatient_admission_uk.v1
    class Meta:
        model = ehrmodels.InpatientAdmission
        # ELEMENT Date of admission
        fields = ['date_of_admission']

class ReasonForEncounterForm(forms.ModelForm):
    # EVALUATION Reason for Encounter [0..*]
    # openEHR-EHR-EVALUATION.reason_for_encounter.v1
    class Meta:
        model = ehrmodels.ReasonForEncounter
        # ELEMENT Presenting Problem [0..*]
        fields = ['presenting_problem']

# SECTION Allergies and adverse reactions [1..1]
# openEHR-EHR-SECTION.allergies_adverse_reactions_rcp.v1

class AllergiesForm(forms.ModelForm):
    class Meta:
        # EVALUATION Adverse reaction [0..*]
        # openEHR-EHR-EVALUATION.adverse_reaction_uk.v1
        model = ehrmodels.AdverseReaction
        fields = [
            'causative_agent',         # ELEMENT Causative agent [1..1] ELEMENT   OR   ELEMENT
            'reaction_snomed_code',    # ELEMENT Reaction
            'date_recorded'            # ELEMENT Date recorded
        ]


# SECTION Medication and medical devices
# openEHR-EHR-SECTION.medication_medical_devices_rcp.v1
#   SECTION Current medication
#   openEHR-EHR-SECTION.current_medication_rcp.v1
    class MedicationStatementForm():
        pass
#   EVALUATION Medication statement [0..*]
#   openEHR-EHR-EVALUATION.medication_statement_uk.v1
#
#     openEHR-EHR-CLUSTER.medication_item.v1
#
#     openEHR-EHR-CLUSTER.medication_event_summary.v1
#
#     ELEMENT Medication name [1..1]
#     ELEMENT Form ELEMENT   OR   ELEMENT
#     ELEMENT Route ELEMENT   OR   ELEMENT
#     ELEMENT Dose amount description
#     ELEMENT Dose timing description
#     ELEMENT
#     ELEMENT Monitoring [0..*]
#     ELEMENT Course status
#     ELEMENT Indication
#     ELEMENT Comment / recommendation [0..*]
#
#     CLUSTER First authorised
#       ELEMENT Date first authorised
#     CLUSTER Last administered
#       ELEMENT Date last administered
#     CLUSTER Administration details
#     CLUSTER Product
#       ELEMENT Expiry date
#       ELEMENT Batch number
#     CLUSTER Changed
#       ELEMENT Date changed
#     CLUSTER Medication change detail
#     CLUSTER Adjustment
#       ELEMENT Reason adjusted
#     CLUSTER Last dispensed
#       ELEMENT Date last dispensed
#     CLUSTER Last dispensed details
#     CLUSTER Product
#     CLUSTER Quantity dispensed
#       ELEMENT Quantity description
#     CLUSTER Discontinued
#       ELEMENT Date discontinued
#     CLUSTER Discontinued details
#     CLUSTER Discontinutation
#       ELEMENT Reason discontinued [0..*]


# SECTION Diagnoses [0..*]
#   EVALUATION Problem/diagnosis summary [0..*]
#   openEHR-EHR-EVALUATION.problem_diagnosis.v1
#     ELEMENT Diagnosis [1..1]
#     ELEMENT Clinical description
#     ELEMENT Date/time clinically recognised
#     ELEMENT Comment
#     ELEMENT Last updated
#
# SECTION Problems and issues [0..*]
#   EVALUATION Problem/diagnosis summary [0..*]
#   openEHR-EHR-EVALUATION.problem_diagnosis.v1
#     ELEMENT Diagnosis [1..1]
#     ELEMENT Clinical description
#     ELEMENT Date/time clinically recognised
#     ELEMENT Comment
#     ELEMENT Last updated
#
# SECTION Clinical Summary [0..*]
#   EVALUATION Clinical Synopsis [0..*]
#   openEHR-EHR-EVALUATION.clinical_synopsis.v1
#     ELEMENT Summary [1..1]
