from django.contrib import admin

from hospital.models import Diagnosis, Doctor, Patient, Surgery


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    pass


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "birth_year", "position", "speciality")
    list_filter = ("position", "speciality")


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "survived")
    list_filter = ("survived",)


@admin.register(Surgery)
class SurgeryAdmin(admin.ModelAdmin):
    list_display = ("id", "start_datetime", "end_datetime")
