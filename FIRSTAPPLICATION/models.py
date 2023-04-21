from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=255)
    
    def __str__(self) :
        return f'{self.name}   {self.phone}     {self.email}'