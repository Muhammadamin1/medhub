from django.urls import path, include

urlpatterns = [
    path('questionnaire/', include('api.v1.questionnaire.urls')),
    path('user/', include('api.v1.user.urls'))
]