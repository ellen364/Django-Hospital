![Django Hospital](./django_hospital_logo.png)

An easy, interactive way to practice Django queries. Great for beginners.

* A Django app - learn with the tools you want to use
* Fictional hospital (familiar to some!) with doctors, patients, diagnoses, and surgeries
* Pull out the right data and test failures become test successes
* Challenge yourself to complete every example query

## Getting Started

These instructions will get Django Hospital up and running on your local machine.

### Prerequisites

* Python
* Django
* Git

To install Django (and Python if you need it) on Windows: https://docs.djangoproject.com/en/2.0/howto/windows/

For Linux or Mac: https://docs.djangoproject.com/en/2.0/topics/install/

To install Git on any operating system: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

### Installing

Get started with just 1 line of code.

(Though remember to make sure you're in the directory where you want to clone the project!)

```
git clone https://github.com/ellen654321/Django-Hospital.git
```

## Using Django Hospital

Have a look in models.py to get familiar with the 4 models (Doctor, Patient, Diagnosis, Surgery)

Open user_queries.py and start working through the practice queries. Just replace "False" with your answer.
```
def all_doctors():
    return False
```

Whenever you want to check your answers, run the tests and watch the number of fails steadily fall to 0 :)
```
python manage.py test
```

If you'd rather run a single test, you can do that too. Replace the last part of this example ("test_all_doctors") with the test method you want to run.
```
python manage.py test hospital.tests.HospitalTests.test_all_doctors
```
The format is always "test_" followed by the name of the function in user_queries.py

## How you can help

Django Hospital is a way to give something back :sunflower:

Fantastic people created amazing, free resources that I've benefited from since starting to learn Django a few months ago and Python a little before that. Hopefully this project will help a few people, just as I was helped.

It's always useful to hear what worked and what didn't, which sections are too long or not long enough, what's kind of confusing, what you'd like to see more of. So if you've got a few minutes, let me know :sun_with_face:

* Report a bug -- if you spot a mistake or something isn't working, open an issue here on Github
* Give feedback -- general feedback and suggestions are welcome. Please send them to djangohospital@gmail.com
* Tell a friend -- if you've found Django Hospital useful, chances are other people will too
* *Coming soon* -- a CONTRIBUTING.md and "help wanted" labels on issues, so people can directly contribute to improving Django Hospital

## Authors

* **Ellen** [(ellen654321)](https://github.com/ellen654321/) -- *initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Built With

* [Django](https://www.djangoproject.com/)

## Acknowledgments

* Grey's Anatomy is owned by ABC and was created by Shonda Rhimes
* Information from the [Grey's Anatomy Universe Wiki](http://greysanatomy.wikia.com/wiki/Grey%27s_Anatomy_Universe_Wiki) was used to create the test data, with a little guessing from me (e.g. where intern birth years weren't available)
* PurpleBooth's [README-Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) provided the initial outline for this README
