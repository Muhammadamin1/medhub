from django.contrib import admin
from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'title', 'is_true']


admin.site.register(Answer, AnswerAdmin)