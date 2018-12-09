from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
    password = models.IntegerField(default='0')


class User(models.Model):
    name = models.CharField('姓名',max_length=20)
    password = models.CharField('密码',max_length=16)
    age = models.IntegerField()

class User2(models.Model):
    name = models.CharField('姓名',max_length=20)
    password = models.CharField('密码',max_length=16)
    age = models.IntegerField()
    class Meta:
        db_table = "User2"
