from rest_framework import serializers

from questionnaire.models import Question, Answer, SubQuestion


# ------------------ QUESTION ----------------------------

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


# --------------------- ANSWER ----------------------------


class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'question',
            'title',
            'is_true'
        ]


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'question',
            'title',
            'is_true'
        ]


# ------------------ SUB QUESTION ----------------------------


class SubQuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubQuestion
        fields = [
            'id',
            'question',
            'answer',
            'title',
        ]


class SubQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubQuestion
        fields = [
            'question',
            'answer',
            'title',
        ]
