from django.db import models
from exam.models import ECECoreSubject
# Create your models here.

class Question(models.Model):
    text                   = models.CharField(max_length= 256)
    ece_coresubject        = models.ForeignKey(ECECoreSubject, on_delete=models.CASCADE)
    created                = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=256)
    correct =models.BooleanField(default=False)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'question : {self.questions.text}, answer: {self.text} correct: {self.correct}'