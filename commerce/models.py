from django.db import models

# Create your models here.
class RegistersUser(models.Model):
    name = models.CharField(max_length=100)
    emailId = models.CharField(max_length=100)
    phoneNum = models.CharField(blank=True, null=True, max_length=20)
    password = models.CharField(max_length=30)