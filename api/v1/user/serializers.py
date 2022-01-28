from rest_framework import serializers
from user.models import Interrogator, Responder


class InterrogatorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interrogator
        fields = [
            'id',
            'username',
            'photo',
            'email',
        ]


class InterrogatorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interrogator
        fields = [
            'username',
            'photo',
            'email',
        ]


class ResponderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responder
        fields = [
            'id',
            'username',
            'birth_date',
            'gender',
            'photo',
            'email',
        ]


class ResponderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responder
        fields = [
            'username',
            'birth_date',
            'gender',
            'photo',
            'email',
        ]
