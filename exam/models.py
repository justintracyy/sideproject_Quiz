from django.db import models

# Create your models here.


class ECECoreSubject(models.Model):
    topic                   = models.CharField(max_length= 256)
    number_of_questions     = models.IntegerField()
    require_score_to_pass   = models.IntegerField()

    def __str__(self):
        return f'{self.topic}'

    def get_question(self):
        return  self.question_set.all()



