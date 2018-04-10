import datetime

from hospital.models import Doctor, Patient, Diagnosis, Surgery


def create_test_data():
    doctors = [
        {
            'first_name': 'Meredith',
            'last_name': 'Grey',
            'birth_year': 1978,
            'position': 'INT',
            'speciality': 'GEN',
        },
        {
            'first_name': 'Christina',
            'last_name': 'Yang',
            'birth_year': 1978,
            'position': 'INT',
            'speciality': 'CAR',
        },
        {
            'first_name': 'Izzie',
            'last_name': 'Stevens',
            'birth_year': 1980,
            'position': 'INT',
            'speciality': 'GEN',
        },
        {
            'first_name': 'Alex',
            'last_name': 'Karev',
            'birth_year': 1978,
            'position': 'INT',
            'speciality': 'PED',
        },
        {
            'first_name': 'George',
            'last_name': 'O\'Malley',
            'birth_year': 1980,
            'position': 'INT',
            'speciality': 'GEN',
        },
        {
            'first_name': 'Miranda',
            'last_name': 'Bailey',
            'birth_year': 1973,
            'position': 'RES',
            'speciality': 'GEN',
        },
        {
            'first_name': 'Richard',
            'last_name': 'Webber',
            'birth_year': 1954,
            'position': 'ATT',
            'speciality': 'GEN',
        },
        {
            'first_name': 'Preston',
            'last_name': 'Burke',
            'birth_year': 1966,
            'position': 'ATT',
            'speciality': 'CAR',
        },
        {
            'first_name': 'Derek',
            'last_name': 'Shepherd',
            'birth_year': 1966,
            'position': 'ATT',
            'speciality': 'NEU',
        },
    ]

    patients = [
        {
            'first_name': 'Katie',
            'last_name': 'Bryce',
            'survived': True,
            'diagnoses': [
                'Aneurysm',
                'Subarachnoid hemorrhage'
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 3, 27, 12, 30),
                    'end_datetime': datetime.datetime(2005, 3, 27, 16, 30),
                    'procedure': 'Aneurysm clip',
                    'doctors': [
                        'grey',
                        'shepherd',
                    ]
                },
            ]
        },
        {
            'first_name': 'Tony',
            'last_name': 'Savitch',
            'survived': False,
            'diagnoses': [
                'Coronary heart disease',
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 3, 27, 10, 00),
                    'end_datetime': datetime.datetime(2005, 3, 27, 15, 15),
                    'procedure': 'Coronary artery bypass surgery',
                    'doctors': [
                        'o\'malley',
                        'burke'
                    ]
                }
            ]
        },
        {
            'first_name': 'Bryan',
            'last_name': 'Johnson',
            'survived': True,
            'diagnoses': [
                'Tetralogy of fallot with pulmonary atresia',
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 4, 3, 16, 00),
                    'end_datetime': datetime.datetime(2005, 4, 3, 17, 45),
                    'procedure': 'Transventricular repair with a right ventriculotomy',
                    'doctors': [
                        'grey',
                        'burke'
                    ]
                }
            ]
        },
        {
            'first_name': 'Allison',
            'last_name': '',
            'survived': True,
            'diagnoses': [
                'Blunt head trauma',
                'Defensive wounds',
                'Abdominal rupture',
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 4, 3, 9, 15),
                    'end_datetime': datetime.datetime(2005, 4, 3, 12, 15),
                    'procedure': 'Craniotomy',
                    'doctors': [
                        'grey',
                        'burke',
                        'shepherd'
                    ]
                }
            ]
        },
        {
            'first_name': 'Vic',
            'last_name': '',
            'survived': True,
            'diagnoses': [
                'Amputated penis',
                'Severe loss of blood',
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 4, 3, 20, 20),
                    'end_datetime': datetime.datetime(2005, 4, 3, 21, 50),
                    'procedure': 'Surgery',
                    'doctors': [
                        'grey',
                        'bailey',
                        'yang'
                    ]
                }
            ]
        },
        {
            'first_name': 'Viper',
            'last_name': '',
            'survived': True,
            'diagnoses': [
                'Abdominal lacerations',
                'Internal bleeding',
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 4, 10, 11, 45),
                    'end_datetime': datetime.datetime(2005, 4, 10, 13, 45),
                    'procedure': 'Surgery',
                    'doctors': [
                        'grey',
                        'bailey'
                    ]
                }
            ]
        },
        {
            'first_name': 'Kevin',
            'last_name': 'Davidson',
            'survived': False,
            'diagnoses': [
                'Widened mediastinum',
                'Cerebral edema',
                'Traumatic aortic injury',
                'Brain death',
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 4, 10, 10, 00),
                    'end_datetime': datetime.datetime(2005, 4, 10, 17, 00),
                    'procedure': 'Aortic repair',
                    'doctors': [
                        'stevens',
                        'yang',
                        'burke',
                        'shepherd'
                    ]
                },
                {
                    'start_datetime': datetime.datetime(2005, 4, 10, 20, 15),
                    'end_datetime': datetime.datetime(2005, 4, 10, 22, 15),
                    'procedure': 'Organ harvest',
                    'doctors': [
                        'stevens',
                        'yang',
                        'burke',
                        'shepherd'
                    ]
                },
            ]
        },
        {
            'first_name': 'Lloyd',
            'last_name': 'Mackie',
            'survived': True,
            'diagnoses': [
                'Liver cancer',
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 4, 10, 22, 30),
                    'end_datetime': datetime.datetime(2005, 4, 11, 5, 15),
                    'procedure': 'Liver transplant',
                    'doctors': [
                        'o\'malley',
                        'webber'
                    ]
                }
            ]
        },
        {
            'first_name': 'Rick',
            'last_name': 'Humphrey',
            'survived': True,
            'diagnoses': [
                'Prostate cancer',
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 4, 17, 13, 45),
                    'end_datetime': datetime.datetime(2005, 4, 17, 16, 00),
                    'procedure': 'Prostatectomy',
                    'doctors': [
                        'stevens',
                        'o\'malley',
                        'bailey'
                    ]
                }
            ]
        },
        {
            'first_name': 'Jorge',
            'last_name': 'Cruz',
            'survived': True,
            'diagnoses': [
                'Sharp force trauma',
                'Brain tumour',
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 4, 17, 10, 00),
                    'end_datetime': datetime.datetime(2005, 4, 17, 12, 25),
                    'procedure': 'Controlled extraction',
                    'doctors': [
                        'grey',
                        'o\'malley',
                        'karev',
                        'shepherd'
                    ]
                },
                {
                    'start_datetime': datetime.datetime(2005, 4, 17, 17, 30),
                    'end_datetime': datetime.datetime(2005, 4, 17, 20, 40),
                    'procedure': 'Tumor resection',
                    'doctors': [
                        'grey',
                        'o\'malley',
                        'karev',
                        'shepherd'
                    ]
                }
            ]
        },
        {
            'first_name': '',
            'last_name': 'Patterson',
            'survived': True,
            'diagnoses': [
                'Angina',
                'Tear in the ventricular wall',
                'Anorexia'
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 4, 24, 7, 15),
                    'end_datetime': datetime.datetime(2005, 4, 24, 12, 5),
                    'procedure': 'Coronary artery bypass graft',
                    'doctors': [
                        'grey',
                        'burke'
                    ]
                },
                {
                    'start_datetime': datetime.datetime(2005, 4, 24, 15, 10),
                    'end_datetime': datetime.datetime(2005, 4, 24, 17, 50),
                    'procedure': 'Surgery',
                    'doctors': [
                        'grey',
                        'burke'
                    ]
                }
            ]
        },
        {
            'first_name': 'Stephanie',
            'last_name': 'Drake',
            'survived': True,
            'diagnoses': [
                'Hyperinflated lungs',
                'Foreign object in lung',
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 4, 24, 9, 30),
                    'end_datetime': datetime.datetime(2005, 4, 24, 11, 55),
                    'procedure': 'Foreign body removal',
                    'doctors': [
                        'o\'malley',
                        'bailey',
                        'webber'
                    ]
                }
            ]
        },
        {
            'first_name': 'Jerry',
            'last_name': 'Frost',
            'survived': True,
            'diagnoses': [
                'Chronic back pain',
                'Drug addiction',
                'Spinal fusion',
                'Subdural bleed with midline shift',
            ],
            'surgeries': [
                {
                    'start_datetime': datetime.datetime(2005, 4, 24, 14, 50),
                    'end_datetime': datetime.datetime(2005, 4, 24, 18, 15),
                    'procedure': 'Brain surgery',
                    'doctors': [
                        'karev',
                        'stevens',
                        'shepherd'
                    ]
                }
            ]
        },
    ]
    # http://greysanatomy.wikia.com/wiki/Season_1_(Grey%27s_Anatomy)
    # Next episode:
    # http://greysanatomy.wikia.com/wiki/If_Tomorrow_Never_Comes

    for doctor in doctors:
        Doctor.objects.create(
            first_name=doctor['first_name'],
            last_name=doctor['last_name'],
            birth_year=doctor['birth_year'],
            position=doctor['position'],
            speciality=doctor['speciality'])

    for patient in patients:
        p = Patient.objects.create(
            first_name=patient['first_name'],
            last_name=patient['last_name'],
            survived=patient['survived'])
        print('patient: ', p)

        for diagnosis in patient['diagnoses']:
            Diagnosis.objects.create(description=diagnosis, patient=p)

        for surgery in patient['surgeries']:
            s = Surgery.objects.create(
                start_datetime=surgery['start_datetime'],
                end_datetime=surgery['end_datetime'],
                procedure=surgery['procedure'],
                patient=p)
            print('surgery: ', s)

            for doctor in surgery['doctors']:
                d = Doctor.objects.get(last_name__iexact=doctor)
                print('doctor: ', d)
                s.doctors.add(d)
