from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    
    class Meta:
        db_table='students'