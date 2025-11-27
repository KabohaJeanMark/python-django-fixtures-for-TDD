from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name