from django.db import models


class Passenger(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True, blank=False)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.name


class Survey(models.Model):
    passengers = models.ManyToManyField(Passenger)
    name = models.CharField(max_length=250)
    date_from = models.DateTimeField(blank=False)
    date_to = models.DateTimeField(blank=False)

    def __str__(self):
        return f'{self.name} ({self.date_from} - {self.date_to})'


class Question(models.Model):
    surveys = models.ManyToManyField(Survey, related_name='questions')
    TYPE_CHOICES = [
        ('RA', 'Radio'),
        ('MU', 'Multiple'),
        ('FT', 'Free text')
    ]
    survey_type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default='FT'
    )
    title = models.CharField(max_length=500)
    other = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='choices',
        on_delete=models.CASCADE
    )
    text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.text} ({self.question.title})'


class Feedback(models.Model):
    passenger = models.ForeignKey(
        Passenger,
        related_name='feedback',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    RATING_CHOICES = [
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars'),
    ]
    rating = models.CharField(
        max_length=2,
        choices=RATING_CHOICES,
        default='5'
    )

    def __str__(self):
        return self.passenger.name


class SurveyResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question.title


class ResponseText(SurveyResponse):
    answer = models.TextField(blank=True)
