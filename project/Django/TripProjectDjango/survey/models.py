from django.db import models


# Create your models here.
class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True)
    survey_question = models.CharField(max_length=100)
    survey_choices = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'survey'

    def choices_split(self):
        return self.survey_choices.split(",")

    def __str__(self):
        return self.survey_idx, ",", self.survey_question, ",", self.survey_choices