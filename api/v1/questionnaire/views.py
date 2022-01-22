from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView


class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer

