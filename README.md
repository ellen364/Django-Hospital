![Django Hospital](./django_hospital_logo.png)

Django Hospital is an interactive way to practice Django queries.

## Features

* For Django 3.1
* Provides data for a fictional hospital -- doctors, patients, diagnoses and surgeries
* Uses Python's built in testing tools (unittest)
* Start with 20 failing tests. Write your queries in `tests.py` and watch test failures turn into test successes

## Installing

To install Django Hospital:
* Clone the repo
* Install the requirements in `requirements/base.txt`

## Using Django Hospital

Have a look in `hospital/models.py` to get familiar with the 4 models (Doctor, Patient, Diagnosis, Surgery).

Open `hospital/tests.py` and start working through the practice queries.

Each test has the structure below. The docstring explains what data you should retrieve with your query. The first argument to `assertQuerysetEqual`, "Replace with your query", is where your query goes. The second argument, `queries.all_doctors()` in this case, is the value against which your query will be compared.
```python
def test_all_doctors(self):
    """Retrieve every doctor."""
    self.assertQuerysetEqual(
        "Replace with your query",
        queries.all_doctors(),
    )
```

Whenever you want to check your answers, run the tests.
```
python manage.py test
```

## Using the shell or admin

To explore the data using the shell or admin, you'll need to setup the local database and import the data. (The test framework imports the data for each test run, so you only need to follow these steps if you want to use the shell or admin.)

```
python manage.py migrate
python manage.py loaddata hospital/fixtures/initial_data.json
```

To access the Django admin, you also need to create a user.
```
python manage.py createsuperuser
```

## Acknowledgments

* Grey's Anatomy is owned by ABC and was created by Shonda Rhimes.
* Information from the [Grey's Anatomy Universe Wiki] was used to create the fixtures, with a little guessing from me (e.g. where intern birth years weren't available).

[issue]: https://github.com/ellen364/Django-Hospital/issues/new
[Grey's Anatomy Universe Wiki]: http://greysanatomy.wikia.com/wiki/Grey%27s_Anatomy_Universe_Wiki
