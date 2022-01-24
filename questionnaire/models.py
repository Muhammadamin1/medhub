from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    is_true = models.BooleanField()

    def __str__(self):
        return self.title


class SubQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title
