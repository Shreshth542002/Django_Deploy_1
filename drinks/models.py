from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name + ' ' + self.description 