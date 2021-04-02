import datetime

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Choice
from api.models import Feedback
from api.models import Passenger
from api.models import Question
from api.models import ResponseText
from api.models import Survey

from api.serializers import FeedbackSerializer
from api.serializers import SurveySerializer

ERROR = {
    'errors': True,
    'msg': 'There was a problem with your request.'
}

NO_PASSENGER = {
    'errors': True,
    'msg': 'Passenger does not exist.'
}


class FeedbackViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new feedback instance.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    http_method_names = ['post']

    def create(self, request):
        rating = request.data.get('rating', None)
        survey = request.data.get('survey', {})
        user = request.data.get('user', None)

        try:
            passenger = Passenger.objects.get(email=user)
        except Exception:
            return Response(NO_PASSENGER, status=status.HTTP_400_BAD_REQUEST)

        feedback = Feedback()
        feedback.passenger = passenger

        if rating is not None:
            feedback.rating = rating

        feedback.save()

        for question in survey:
            response = ResponseText()

            try:
                question_obj = Question.objects.get(id=question)
            except Exception:
                return Response(ERROR, status=status.HTTP_400_BAD_REQUEST)

            response.question = question_obj
            response.feedback = feedback

            text = survey[question]

            if isinstance(survey[question], list):
                answer_text = []
                for selection in survey[question]:
                    choice = Choice.objects.get(id=selection)
                    answer_text.append(choice.text)

                text = ', '.join(answer_text)

            response.answer = text
            response.save()

        data = {'errors': False, 'msg': 'Thank you for your feedback!'}

        return Response(data, status=status.HTTP_201_CREATED)


class SurveyViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all surveys.
    """
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        return self.queryset.all()

    def list(self, request):
        user = request.query_params.get('user', None)

        if user is None:
            return Response(ERROR, status=status.HTTP_400_BAD_REQUEST)

        today = datetime.date.today()

        # Get user.
        # In a production system this would be
        # the user object from the http request
        try:
            passenger = Passenger.objects.get(email=user)
        except Exception:
            return Response(NO_PASSENGER, status=status.HTTP_400_BAD_REQUEST)

        # Get survey for logged in user
        queryset = self.get_queryset()

        response = self.get_serializer(
            queryset.filter(
                date_from__lte=today,
                date_to__gte=today,
                passengers__in=(str(passenger.pk))
            ),
            many=True
        ).data

        return Response(response, status=status.HTTP_200_OK)
