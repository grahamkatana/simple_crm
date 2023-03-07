from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=25)
    last_name =models.CharField(max_length=25)
    address =  models.CharField(max_length=250)
    city =  models.CharField(max_length=25)
    email =  models.EmailField(max_length=25)
    phone =  models.CharField(max_length=13)
    postal_code =  models.CharField(max_length=10)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
