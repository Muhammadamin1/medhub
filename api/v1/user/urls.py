from django.urls import path
from .views import *

urlpatterns = [
    # Interrogator
    path('interrogator/list/', InterrogatorListAPIView.as_view()),
    path('interrogator/create/', InterrogatorCreateAPIView.as_view()),

    # Responder
    path('responder/list/', ResponderListAPIView.as_view()),
    path('responder/create/', ResponderCreateAPIView.as_view()),

]
