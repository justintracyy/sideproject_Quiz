from django.db import models
from exam.models import ECECoreSubject
from django.contrib.auth.models import User
# Create your models here.

class Result(models.Model):
    quiz = models.ForeignKey(ECECoreSubject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)