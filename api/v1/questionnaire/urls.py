from django.urls import path
from .views import *

urlpatterns = [
    path('question/list/', QuestionListAPIView.as_view())
]