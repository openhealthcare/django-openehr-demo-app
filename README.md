# Django-openEHR Demo Application
alpha | unsupported

heroku link

This repository contains a demo application for the [django-openehr](https://pypi.python.org/pypi/django_openehr) models library.

To try this application:

* `git clone` this repo into a suitable folder
* `cd` into the cloned directory
* (create a new virtualenv, if you are a virtualenv user)
* `pip install -r requirements.txt` to install dependencies
* `python manage.py migrate` to set up the database
* `python manage.py createsuperuser` (enter some super user details)
* `python manage.py runserver`

* navigate to localhost:8000/admin/ to log in and interact with the models using the Django admin interface.

* You can also use the Django shell (`python manage.py shell` to manipulate the new classes.)

-----

# IDCR Transfer of Care summary (minimal)
#### Human-readable transliteration

## SECTION Relevant contacts [0..*]
openEHR-EHR-SECTION.relevant_contacts_rcp.v1
  ### ADMIN_ENTRY Relevant contact [0..*]
  openEHR-EHR-ADMIN_ENTRY.relevant_contact_rcp.v0

  ### CLUSTER Personal details
  openEHR-EHR-CLUSTER.individual_professional_uk.v1
    #### CLUSTER Person name
    openEHR-EHR-CLUSTER.person_name.v1
      ELEMENT Full name
    #### CLUSTER Telecom details
    openEHR-EHR-CLUSTER.telecom_uk.v1
      ELEMENT Telcoms

  ELEMENT Professional group
  ELEMENT Relationship category
  ELEMENT Relationship
  ELEMENT Is next of kin?
  ELEMENT Note
  ELEMENT Date updated

## SECTION Admission details [0..*]
openEHR-EHR-SECTION.admission_details_rcp.v1
  ### ADMIN_ENTRY Inpatient admission [0..*]
  openEHR-EHR-ADMIN_ENTRY.inpatient_admission_uk.v1
    ELEMENT Date of admission

  ### EVALUATION Reason for Encounter [0..*]
  openEHR-EHR-EVALUATION.reason_for_encounter.v1
    ELEMENT Presenting Problem [0..*]

## SECTION Allergies and adverse reactions [1..1]
openEHR-EHR-SECTION.allergies_adverse_reactions_rcp.v1
  ### EVALUATION Adverse reaction [0..*]
  openEHR-EHR-EVALUATION.adverse_reaction_uk.v1
    ELEMENT Causative agent [1..1] ELEMENT   OR   ELEMENT
    ELEMENT Reaction
    ELEMENT Date recorded

## SECTION Medication and medical devices
openEHR-EHR-SECTION.medication_medical_devices_rcp.v1
  ### SECTION Current medication
  openEHR-EHR-SECTION.current_medication_rcp.v1
  ### EVALUATION Medication statement [0..*]
  openEHR-EHR-EVALUATION.medication_statement_uk.v1

    * ELEMENT Medication name [1..1]
    * ELEMENT Form ELEMENT   OR   ELEMENT
    * ELEMENT Route ELEMENT   OR   ELEMENT
    * ELEMENT Dose amount description
    * ELEMENT Dose timing description
    * ELEMENT
    * ELEMENT Monitoring [0..*]
    * ELEMENT Course status
    * ELEMENT Indication
    * ELEMENT Comment / recommendation [0..*]
    * CLUSTER First authorised
      * ELEMENT Date first authorised
    * CLUSTER Last administered
      * ELEMENT Date last administered
    * CLUSTER Administration details
    * CLUSTER Product
      * ELEMENT Expiry date
      * ELEMENT Batch number
    * CLUSTER Changed
      * ELEMENT Date changed
    * CLUSTER Medication change detail
    * CLUSTER Adjustment
      * ELEMENT Reason adjusted
    * CLUSTER Last dispensed
      * ELEMENT Date last dispensed
    * CLUSTER Last dispensed details
    * CLUSTER Product
    * CLUSTER Quantity dispensed
      * ELEMENT Quantity description
    * CLUSTER Discontinued
      * ELEMENT Date discontinued
    * CLUSTER Discontinued details
    * CLUSTER Discontinutation
      * ELEMENT Reason discontinued [0..*]

## SECTION Diagnoses [0..*]
  ### EVALUATION Problem/diagnosis summary [0..*]
  openEHR-EHR-EVALUATION.problem_diagnosis.v1
    * ELEMENT Diagnosis [1..1]
    * ELEMENT Clinical description
    * ELEMENT Date/time clinically recognised
    * ELEMENT Comment
    * ELEMENT Last updated

## SECTION Problems and issues [0..*]
  ### EVALUATION Problem/diagnosis summary [0..*]
  openEHR-EHR-EVALUATION.problem_diagnosis.v1
    * ELEMENT Diagnosis [1..1]
    * ELEMENT Clinical description
    * ELEMENT Date/time clinically recognised
    * ELEMENT Comment
    * ELEMENT Last updated

## SECTION Clinical Summary [0..*]
  ### EVALUATION Clinical Synopsis [0..*]
  openEHR-EHR-EVALUATION.clinical_synopsis.v1
    * ELEMENT Summary [1..1]