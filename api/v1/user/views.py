from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import *


class InterrogatorListAPIView(ListAPIView):
    queryset = Interrogator.objects.all()
    serializer_class = InterrogatorListSerializer


class InterrogatorCreateAPIView(CreateAPIView):
    queryset = Interrogator.objects.all()
    serializer_class = InterrogatorCreateSerializer


class ResponderListAPIView(ListAPIView):
    queryset = Responder.objects.all()
    serializer_class = ResponderListSerializer


class ResponderCreateAPIView(CreateAPIView):
    queryset = Responder.objects.all()
    serializer_class = ResponderCreateSerializer
