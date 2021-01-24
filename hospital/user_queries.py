from hospital.models import Diagnosis, Doctor, Patient, Surgery


# Getting used to the models
# Retrieve every doctor
def all_doctors():
    # Replace "False" with your query
    return False


# Retrieve the doctors who are attendings
def all_attendings():
    return False


# Retrieve only the doctor Meredith Grey
def meredith_grey():
    return False


# Retrieve patients who died
def deceased_patients():
    return False


# Working with field lookups
# https://docs.djangoproject.com/en/2.0/ref/models/querysets/#field-lookups
# Retrieve surgeries in which the procedure includes the word 'surgery', ignoring case
def procedure_contains_surgery_case_insensitive():
    return False


# Retrieve surgeries in which the procedure includes the word 'Surgery', case specific
def procedure_contains_surgery_case_sensitive():
    return False


# Retrieve patients whose first name appears in the following list: ['Katie', 'Kevin', 'Rick']
def patients_with_certain_first_names():
    return False


# Retrieve doctors born in the following years: 1954, 1973
def doctors_born_in_certain_years():
    return False


# Retrieve doctors who are interns and born after 1978
def interns_born_after_1978():
    return False


# Retrieve surgeries occurring on 10 April 2005 but starting before noon
def surgeries_on_10_apr_2005_starting_before_noon():
    return False


# Spanning relationships
# https://docs.djangoproject.com/en/2.0/topics/db/queries/#lookups-that-span-relationships
# Retrieve all of Dr Bailey's surgeries
def baileys_surgeries():
    return False


# Retrieve all cardiothoracic surgeries
def cardiothoracic_surgeries():
    return False


# Retrieve patients treated by Dr Shepherd
# (remember: patients can have >1 surgery)
def shepherds_patients():
    return False


# Aggregate queries
# https://docs.djangoproject.com/en/2.0/topics/db/aggregation/
# How many patients died?
def number_deceased_patients(self):
    return False


# How many diagnoses were received patient Jerry Frost?
def number_of_diagnosis_jerry_frost(self):
    return False


# Of the doctors' birth years, what is the earliest year?
def earliest_birth_year_of_doctors(self):
    return False


# What is the largest number of diagnoses received by a patient?
def largest_number_of_diagnoses(self):
    return False


# Extra credit - these queries are quite a bit harder and might be too big a jump
# What is the average duration of all surgeries?
# (tip: if you're using SQLite, the default database for this app, you'll need to use an ExpressionWrapper)
def average_duration_all_surgeries(self):
    return False


# Retrieve surgeries that took >3 hours
def surgeries_longer_3hours():
    return False
