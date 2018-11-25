import datetime
from django.test import TestCase
from django.db.models import Avg, Count, Max, Min, DurationField, ExpressionWrapper, F

import hospital.test_data as test_data
import hospital.user_queries as user_queries
from hospital.models import Doctor, Patient, Diagnosis, Surgery


class HospitalTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_data.create_test_data()

    def test_all_doctors(self):
        qs = Doctor.objects.all()
        self.assertListEqual(
            list(qs),
            list(user_queries.all_doctors()))

    def test_all_attendings(self):
        qs = Doctor.objects.filter(position='ATT')
        self.assertListEqual(
            list(qs),
            list(user_queries.all_attendings()))

    def test_meredith_grey(self):
        instance = Doctor.objects.get(first_name='Meredith')
        self.assertEqual(
            instance,
            user_queries.meredith_grey())

    def test_deceased_patients(self):
        qs = Patient.objects.filter(survived=False)
        self.assertListEqual(
            list(qs),
            list(user_queries.deceased_patients()))

    def test_procedure_contains_surgery_case_insensitive(self):
        qs = Surgery.objects.filter(procedure__icontains='surgery')
        self.assertListEqual(
            list(qs),
            list(user_queries.procedure_contains_surgery_case_insensitive()))

    def test_procedure_contains_surgery_case_sensitive(self):
        qs = Surgery.objects.filter(procedure__contains='Surgery')
        self.assertListEqual(
            list(qs),
            list(user_queries.procedure_contains_surgery_case_sensitive()))

    def test_patients_with_certain_first_names(self):
        qs = Patient.objects.filter(first_name__in=['Katie', 'Kevin', 'Rick'])
        self.assertListEqual(
            list(qs),
            list(user_queries.patients_with_certain_first_names()))

    def test_doctors_born_in_certain_years(self):
        qs = Doctor.objects.filter(birth_year__in=[1954, 1973])
        self.assertListEqual(
            list(qs),
            list(user_queries.doctors_born_in_certain_years()))

    def test_interns_born_after_1978(self):
        qs = Doctor.objects.filter(birth_year__gt=1978, position='INT')
        self.assertListEqual(
            list(qs),
            list(user_queries.interns_born_after_1978()))

    def test_surgeries_on_10_apr_2005_starting_before_noon(self):
        qs = Surgery.objects.filter(
            start_datetime__gte=datetime.datetime(2005, 4, 10, 0, 0),
            start_datetime__lt=datetime.datetime(2005, 4, 10, 12, 0))
        self.assertListEqual(
            list(qs),
            list(user_queries.surgeries_on_10_apr_2005_starting_before_noon()))

    def test_baileys_surgeries(self):
        qs = Surgery.objects.filter(doctors__last_name="Bailey")
        self.assertListEqual(
            list(qs),
            list(user_queries.baileys_surgeries()))

    def test_cardiothoracic_surgeries(self):
        qs = Surgery.objects.filter(doctors__speciality="CAR")
        self.assertListEqual(
            list(qs),
            list(user_queries.cardiothoracic_surgeries()))

    def test_shepherds_patients(self):
        qs = Patient.objects.filter(
            surgery__doctors__last_name='Shepherd'
        ).distinct()
        self.assertListEqual(
            list(qs),
            list(user_queries.shepherds_patients()))

    def test_number_deceased_patients(self):
        num = Patient.objects.filter(survived=False).count()
        self.assertEqual(
            num,
            user_queries.number_deceased_patients())

    def test_number_of_diagnosis_jerry_frost(self):
        num = Diagnosis.objects.filter(
            patient__first_name='Jerry',
            patient__last_name='Frost'
        ).count()
        self.assertEqual(
            num,
            user_queries.number_of_diagnosis_jerry_frost())

    def test_earliest_birth_year_of_doctors(self):
        dict = Doctor.objects.aggregate(Min('birth_year'))
        self.assertEqual(
            dict,
            user_queries.earliest_birth_year_of_doctors())

    def test_largest_number_of_diagnoses(self):
        dict = Patient.objects.annotate(
            num_diagnoses=Count('diagnosis')
        ).aggregate(Max('num_diagnoses'))

        self.assertEqual(
            dict,
            user_queries.largest_number_of_diagnoses())

    def test_average_duration_all_surgeries(self):
        dict = Surgery.objects.annotate(
            duration=ExpressionWrapper(
                F('end_datetime') - F('start_datetime'), output_field=DurationField())
        ).aggregate(Avg('duration'))

        self.assertEqual(
            dict,
            user_queries.average_duration_all_surgeries())

    def test_surgeries_longer_3hours(self):
        qs = Surgery.objects.annotate(
            duration=ExpressionWrapper(
                F('end_datetime') - F('start_datetime'), output_field=DurationField())
        ).filter(duration__gt=datetime.timedelta(hours=3))

        self.assertListEqual(
            list(qs),
            list(user_queries.surgeries_longer_3hours()))
