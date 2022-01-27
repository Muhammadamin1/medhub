from django.urls import path

from auth.views import MyTokenObtainPairView, RefreshTokenView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', RefreshTokenView.as_view()),

]
