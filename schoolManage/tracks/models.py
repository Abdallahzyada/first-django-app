from django.db import models

class Track(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.name
