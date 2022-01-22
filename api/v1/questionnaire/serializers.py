from rest_framework import serializers

from questionnaire.models import Question


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'title',
        ]

    def sub_question(self, value):
        if value.answer_set.all():
            print(value.answer_set.all())


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'title',
        ]


class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'title',
        ]