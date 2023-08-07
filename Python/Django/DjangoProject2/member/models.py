from django.db import models

# Create your models here.
class Member(models.Model):

    #멤버 변수를 생성해주면,
    # 1. vo의 변수의 역할
    # 2. table 의 항목을 생성
    user_id = models.CharField(max_length=255)
    user_pw = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_tel = models.CharField(max_length=255)

    # java vo 에서의 toString()역할
    def __str__(self):
        return self.user_id + ", "+ \
                self.user_pw + ", " + \
                self.user_name + ", " + \
                self.user_tel