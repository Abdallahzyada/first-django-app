from django.db import models

from tracks.models import Track
# Create your models here.
class Trainee (models.Model):
    id=models.AutoField(primary_key=True,db_column='id')
    name = models.CharField(max_length=50)
    track=models.ForeignKey(Track,on_delete=models.CASCADE,db_column='track_id')
    
    def __str__(self):
        return self.name

