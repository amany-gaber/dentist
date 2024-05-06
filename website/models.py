from django.db import models
from django.core.exceptions import ValidationError

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    schedule = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    message = models.TextField()



    

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='valid_phone_format',
                check=models.Q(phone__regex=r'^\+?1?\d{9,15}$'),
            ),
            models.CheckConstraint(
                name='valid_email',
                check=models.Q(email__regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
            ),
            
        ]


    def __str__(self):
        return self.name
