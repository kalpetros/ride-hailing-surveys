from django.contrib import admin

from api.models import Choice
from api.models import Feedback
from api.models import Question
from api.models import Passenger
from api.models import ResponseText
from api.models import Survey


class ChoiceAdmin(admin.ModelAdmin):
    model = Survey
    list_display = ['text', 'get_question']

    def get_question(self, obj):
        return obj.question.title

    get_question.short_description = 'Question'
    get_question.admin_order_field = 'choice__question'


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    model = Survey
    inlines = [ChoiceInline]
    list_display = ['title', 'get_surveys']

    def get_surveys(self, obj):
        return ', '.join([survey.name for survey in obj.surveys.all()])

    get_surveys.short_description = 'Surveys'
    get_surveys.admin_order_field = 'question__surveys'


class ResponseTextInline(admin.TabularInline):
    model = ResponseText


class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    inlines = [ResponseTextInline]
    list_display = ['passenger', 'created']


class SurveyAdmin(admin.ModelAdmin):
    model = Survey
    list_display = ['name', 'date_from', 'date_to']


class PassengerAdmin(admin.ModelAdmin):
    model = Passenger
    list_display = ['name', 'email']


admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Passenger, PassengerAdmin)
