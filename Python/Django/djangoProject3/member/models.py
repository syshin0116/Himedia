from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ', ' + self.tel + ', ' + self.addr
