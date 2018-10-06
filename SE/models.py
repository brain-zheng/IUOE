from django.db import models

# Create your models here.
class value(models.Model):
    time = models.CharField(max_length=32,null=True)
    dianliu = models.CharField(max_length=32,null=True)
    dianya = models.CharField(max_length=32,null=True)
    dianliang = models.CharField(max_length=32,null=True)
    gonglv = models.CharField(max_length=32,null=True)
    user = models.ForeignKey(to="user_info",to_field="id",on_delete=models.SET_NULL,null=True)

class user_info(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    e_mail = models.CharField(max_length=32)