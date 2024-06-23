from django.db import models

# Create your models here.
class Calculator(models.Model):
    num1 = models.IntegerField(primary_key=True)
    num2 = models.IntegerField()
    choice = models.CharField(max_length=32)