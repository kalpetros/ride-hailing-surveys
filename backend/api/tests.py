from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Feedback
from api.models import Passenger


class FeedbackTestCase(APITestCase):
    def setUp(self):
        passenger = Passenger(
            first_name='John',
            last_name='Doe',
            email='test@test.com'
        )

        passenger.save()

    def test_create_feedback(self):
        """
        Check for feedback creation
        """
        url = 'http://localhost:8000/api/v1/feedback/'
        data = {
            "rating": "4",
            "survey": "",
            "user": "test@test.com",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.count(), 1)

        feedback = Feedback.objects.last()
        rating = feedback.rating
        self.assertEqual(rating, '4')
