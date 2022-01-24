from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView


# ------------------ QUESTION ----------------------------

class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


class QuestionCreateAPIView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer


# ------------------ ANSWER ----------------------------

class AnswerListAPIView(ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer


class AnswerCreateAPIView(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer


# ------------------ SUB QUESTION --------------------------


class SubQuestionListAPIView(ListAPIView):
    queryset = SubQuestion.objects.all()
    serializer_class = SubQuestionListSerializer


class SubQuestionCreateAPIView(CreateAPIView):
    queryset = SubQuestion.objects.all()
    serializer_class = SubQuestionCreateSerializer
