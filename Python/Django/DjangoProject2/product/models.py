from django.db import models

# Create your models here.
class Product(models.Model):

    #멤버 변수를 생성해주면,
    # 1. vo의 변수의 역할
    # 2. table 의 항목을 생성
    product_name = models.CharField(max_length=255)
    product_price = models.CharField(max_length=255)

    # java vo 에서의 toString()역할
    def __str__(self):
        return self.product_name + ", "+ \
                self.product_price