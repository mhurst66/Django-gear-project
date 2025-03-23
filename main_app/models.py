from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

GEARTYPE = (
    ('O', 'Other'),
    ('A', 'Amplifier'),
    ('B', 'Bass'),
    ('G', 'Guitar'),
    ('P', 'Percussion'),
)

class Gear(models.Model):

    type = models.CharField(
        max_length=1,
        choices=GEARTYPE,
        default=GEARTYPE[0][0]
    )
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('gear-detail', kwargs={'gear_id': self.id})
    
    
