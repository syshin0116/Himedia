from django.db import models


# Create your models here.
class Member(models.Model):
    member_idx = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=100, blank=True, null=True)
    member_pw = models.CharField(max_length=100, blank=True, null=True)
    member_naver_token = models.CharField(max_length=100, blank=True, null=True)
    member_google_token = models.CharField(max_length=100, blank=True, null=True)
    member_name = models.CharField(max_length=100)
    member_birth = models.DateField()
    member_addr = models.CharField(max_length=100)
    member_gender = models.IntegerField()
    member_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'member'
        unique_together = (('member_id', 'member_naver_token', 'member_google_token', 'member_name'),)

    def __str__(self):
        return self.member_idx, ',', self.member_id, ',', self.member_pw, + \
               ',', self.member_name, ',', self.member_birth, ',', self.member_addr, + \
               ',', self.member_gender, ',', self.member_naver_token, ',', self.member_google_token, ',', self.member_type
