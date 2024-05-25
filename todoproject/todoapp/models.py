from django.db import models
from django .contrib.auth.models import User
# Create your models here.
class todoform(models.Model):
    taskname=models.CharField(max_length=30)
    priority=models.IntegerField()
    date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)