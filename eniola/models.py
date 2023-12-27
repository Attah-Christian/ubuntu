from django.db import models

# Create your models here.

class UserFormGrabber(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    country = models.CharField(max_length=100)
    message = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return self.firstname + self.lastname
