from django.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from api.views import FeedbackViewSet
from api.views import SurveyViewSet

router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet)
router.register(r'surveys', SurveyViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
