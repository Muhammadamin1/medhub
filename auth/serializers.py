from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        # token['user_level'] = user.level

        return token


class RefreshTokenSerializer(TokenRefreshSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_level"] = user.level
        return token
