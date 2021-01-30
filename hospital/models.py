from django.db import models


class Doctor(models.Model):
    INTERN = "INT"
    RESIDENT = "RES"
    ATTENDING = "ATT"
    POSITION_CHOICES = (
        (INTERN, "Intern"),
        (RESIDENT, "Resident"),
        (ATTENDING, "Attending"),
    )

    GENERAL = "GEN"
    CARDIO = "CAR"
    NEURO = "NEU"
    PEDIATRIC = "PED"
    SPECIALITY_CHOICES = (
        (GENERAL, "General"),
        (CARDIO, "Cardiothoracic"),
        (NEURO, "Neurosurgery"),
        (PEDIATRIC, "Pediatric"),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_year = models.IntegerField()
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    speciality = models.CharField(max_length=3, choices=SPECIALITY_CHOICES)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return "Dr {} {}".format(self.first_name, self.last_name)


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    survived = models.BooleanField(default=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Diagnosis(models.Model):
    description = models.CharField(max_length=200)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Diagnoses"
        ordering = ("id",)


class Surgery(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    procedure = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    doctors = models.ManyToManyField(Doctor)

    class Meta:
        verbose_name_plural = "Surgeries"
        ordering = ("id",)

    def __str__(self):
        return "Surgery at {}".format(self.start_datetime)
