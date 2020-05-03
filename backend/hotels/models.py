from django.db import models

class Package(models.Model):
    hotel = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField() # no of days, thus no of nights = this - 1, unless this is one
    valid_until = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()

    def __str__(self):
        return '{}, {}'.format(self.hotel, self.description)