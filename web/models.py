from django.db import models
# inja mikham az user estefade konam
from django.contrib.auth.models import User
# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Token = models.CharField(max_length=48)
    def __str__(self):
        return "{}__token".format(self.user)
###################################################################
""" #############################################
 in tabe baraye tarife anvae hamalat mibashad """
class EventType(models.Model):
    eventname = models.CharField(max_length=255)
    discription = models.TextField()
    def __str__(self):
        return "{}".format(self.eventname)
##################################################################
class Expense(models.Model):
    text = models.CharField(max_length=250)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
    def __str__(self):
        return "درتاریخ:{} - به مبلغ:{}".format(self.date,self.amount)

class Income(models.Model):
    text = models.CharField(max_length=250)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
    def __str__(self):
        return "درتاریخ:{} - به مبلغ:{}".format(self.date,self.amount)
