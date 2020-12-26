from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Kharg(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date  = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return '{} {} {}'.format(self.user,self.amount,self.text)
class Dakhl(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return '{} {} {}'.format(self.user,self.amount,self.text)