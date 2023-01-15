from django.db import models
class City(models.Model):
    city_text = models.CharField(max_length=200)
    def __str__(self):
        return self.city_text
# Create your models here.
