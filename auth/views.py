from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth.serializers import MyTokenObtainPairSerializer, RefreshTokenSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RefreshTokenView(TokenRefreshView):
    serializer_class = RefreshTokenSerializer
