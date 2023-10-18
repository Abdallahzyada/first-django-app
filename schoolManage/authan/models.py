from django.db import models

# Create your models here.
class MYUser(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=12)