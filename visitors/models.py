from django.db import models


# Create your models here.
class Visitors(models.Model):
    visitorId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    RegisterNumber = models.CharField(max_length=100)
    Email = models.CharField(max_length=150)
    PhoneNumber = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.FirstName} {self.LastName}'
