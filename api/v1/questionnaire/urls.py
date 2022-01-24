from django.urls import path
from .views import *

urlpatterns = [
    # Question
    path('question/list/', QuestionListAPIView.as_view()),
    path('question/create/', QuestionCreateAPIView.as_view()),

    # Answer
    path('answer/list/', AnswerListAPIView.as_view()),
    path('answer/create/', AnswerCreateAPIView.as_view()),

    # SubQuestion
    path('subquestion/list/', SubQuestionListAPIView.as_view()),
    path('subquestion/create/', SubQuestionCreateAPIView.as_view()),
]
