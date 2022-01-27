from django.db import transaction
from rest_framework import serializers

from questionnaire.models import Question, Answer, SubQuestion


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
    answers = serializers.ListSerializer(
        child=AnswerListSerializer(),
        required=False
    )

    class Meta:
        model = Question
        fields = [
            'title',
            'answers'
        ]

    def create(self, validated_data):
        answers = validated_data.pop('answers', [])
        with transaction.atomic():
            question = super().create(validated_data)
            question_info = {'question_id': question.id}
            answers = [Answer(**{**elem, **question_info}) for elem in answers]
            Answer.objects.bulk_create(answers)

        return question

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['answers'] = AnswerListSerializer(instance.answer_set.all(), many=True, context=self.context).data

        return data


class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'title',
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
