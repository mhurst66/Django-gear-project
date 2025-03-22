from django.db import models

GEARTYPE = (
    ('O', 'Other'),
    ('G', 'Guitar'),
    ('B', 'Bass'),
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

    def __str__(self):
        return self.model
    
