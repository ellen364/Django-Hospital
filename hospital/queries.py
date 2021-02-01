from datetime import datetime, timedelta, timezone

from django.db.models import Avg, Count, DurationField, ExpressionWrapper, F, Max, Min

from hospital.models import Diagnosis, Doctor, Patient, Surgery


def all_patients():
    return Patient.objects.all()


def all_doctors():
    return Doctor.objects.all()


def meredith_grey():
    return Doctor.objects.get(first_name="Meredith")


def all_attendings():
    return Doctor.objects.filter(position="ATT")


def patients_unknown_last_name():
    return Patient.objects.filter(last_name="")


def deceased_patients():
    return Patient.objects.filter(survived=False)


def procedure_contains_surgery_case_insensitive():
    return Surgery.objects.filter(procedure__icontains="surgery")


def procedure_contains_surgery_case_sensitive():
    return Surgery.objects.filter(procedure__contains="Surgery")


def patients_with_certain_first_names():
    return Patient.objects.filter(first_name__in=["Katie", "Kevin", "Rick"])


def doctors_born_in_certain_years():
    return Doctor.objects.filter(birth_year__in=[1954, 1973])


def interns_born_after_1978():
    return Doctor.objects.filter(birth_year__gt=1978, position="INT")


def surgeries_on_10_apr_2005_starting_before_noon():
    return Surgery.objects.filter(
        start_datetime__gte=datetime(2005, 4, 10, 0, 0, tzinfo=timezone.utc),
        start_datetime__lt=datetime(2005, 4, 10, 12, 0, tzinfo=timezone.utc),
    )


def baileys_surgeries():
    return Surgery.objects.filter(doctors__last_name="Bailey")


def cardiothoracic_surgeries():
    return Surgery.objects.filter(doctors__speciality="CAR")


def shepherds_patients():
    return Patient.objects.filter(surgery__doctors__last_name="Shepherd").distinct()


def number_deceased_patients():
    return Patient.objects.filter(survived=False).count()


def number_of_diagnoses_jerry_frost():
    return Diagnosis.objects.filter(
        patient__first_name="Jerry", patient__last_name="Frost"
    ).count()


def earliest_birth_year_of_doctors():
    return Doctor.objects.aggregate(Min("birth_year"))


def largest_number_of_diagnoses():
    return Patient.objects.annotate(num_diagnoses=Count("diagnosis")).aggregate(
        Max("num_diagnoses")
    )


def average_duration_all_surgeries():
    return Surgery.objects.annotate(
        duration=ExpressionWrapper(
            F("end_datetime") - F("start_datetime"), output_field=DurationField()
        )
    ).aggregate(Avg("duration"))


def surgeries_longer_3hours():
    return Surgery.objects.annotate(
        duration=ExpressionWrapper(
            F("end_datetime") - F("start_datetime"), output_field=DurationField()
        )
    ).filter(duration__gt=timedelta(hours=3))
