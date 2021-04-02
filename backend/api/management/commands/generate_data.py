import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from api.models import Passenger
from api.models import Survey
from api.models import Question
from api.models import Choice


class Command(BaseCommand):
    help = 'Generates dummy data'

    def create_superuser(self):
        user, created = User.objects.get_or_create(username='test')

        if created:
            self.stdout.write(self.style.NOTICE('[CREATING] - Superuser'))

            user.set_password('test')
            user.is_superuser = True
            user.is_staff = True
            user.save()

            self.stdout.write(self.style.SUCCESS('[CREATED] - Superuser'))

    def create_passenger(self):
        self.stdout.write(self.style.NOTICE('[CREATING] - Passenger'))
        passenger, created = Passenger.objects.get_or_create(
            first_name='John',
            last_name='Doe',
            email='test@test.com'
        )

        self.create_survey(passenger)
        self.stdout.write(self.style.SUCCESS('[CREATED] - Passenger'))

    def create_survey(self, passenger):
        self.stdout.write(self.style.NOTICE('[CREATING] - Survey'))

        date_from = datetime.date(2019, 10, 10)
        date_to = datetime.date(2021, 10, 10)

        survey = Survey(
            name="Driving behavior",
            date_from=date_from,
            date_to=date_to
        )

        survey.save()
        survey.passengers.add(passenger)
        survey.save()
        self.create_questions(survey)
        self.stdout.write(self.style.SUCCESS('[CREATED] - Survey'))

    def create_questions(self, survey):
        self.stdout.write(self.style.NOTICE('[CREATING] - Questions'))

        question_1 = Question(
            survey_type='RA',
            title="How was your overall experience?"
        )

        question_1.save()
        question_1.surveys.add(survey)
        question_1.save()
        self.create_choice(question_1, 'Bad')
        self.create_choice(question_1, 'Great')
        self.create_choice(question_1, 'Awesome')

        question_2 = Question(
            survey_type='MU',
            title='What do you value more?'
        )

        question_2.save()
        question_2.surveys.add(survey)
        question_2.save()
        self.create_choice(question_2, 'Comfortable ride')
        self.create_choice(question_2, 'Experienced driver')
        self.create_choice(question_2, 'New vehicle')

        question_3 = Question(
            survey_type='FT',
            title="Any extra feedback?"
        )

        question_3.save()
        question_3.surveys.add(survey)
        question_3.save()
        self.stdout.write(self.style.SUCCESS('[CREATED] - Questions'))

    def create_choice(self, question, text):
        self.stdout.write(
            self.style.NOTICE(
                f'[CREATING] - Choice for question {question.id}'
            )
        )

        choice = Choice(
            question=question,
            text=text
        )

        choice.save()
        self.stdout.write(
            self.style.SUCCESS(
                f'[CREATED] - Choice for question {question.id}'
            )
        )

    def handle(self, *args, **options):
        self.create_superuser()
        self.create_passenger()
