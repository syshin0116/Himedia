from django.db import models

# Create your models here.
from member.models import Member


class SurveyResult(models.Model):
    surveyResult_idx = models.AutoField(db_column='surveyResult_idx', primary_key=True)  # Field name made lowercase.
    member_idx = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_idx')
    surveyResult_date = models.DateTimeField(db_column='surveyResult_date')  # Field name made lowercase.
    surveyResult_recommendation = models.CharField(db_column='surveyResult_recommendation', max_length=100)  # Field name made lowercase.
    surveyResult_answers = models.CharField(db_column='surveyResult_answers', max_length=100)  # Field name made lowercase.
    surveyResult_rarea = models.CharField(db_column='surveyResult_rarea', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'surveyResult'

    def __str__(self):
        return self.surveyResult_idx, ', ', self.member_idx, ', ', self.surveyResult_date, ', ', self.surveyResult_answers, \
               self.surveyResult_recommendation, ', ', self.surveyResult_rarea

    def choices_split(self):
        return self.choices.split(",")
