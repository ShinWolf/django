from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class RegistersUser(models.Model):
    name = models.CharField(max_length=100)
    emailId = models.CharField(max_length=100)
    phoneNum = models.CharField(blank=True, null=True, max_length=20)
    password = models.CharField(max_length=30)

class RegistersAvis(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    dateAvis = models.DateTimeField(default=timezone.now)
    autheur = models.ForeignKey(User, on_delete=models.CASCADE)