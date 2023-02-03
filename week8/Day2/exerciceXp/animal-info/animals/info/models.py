from django.db import models

class Family(models.Model):
    last_name = models.CharField(max_length=30)


class Animal(models.Model):
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

# a = Family(last_name = "azer")
# q = Animal(legs = 4, weight = 5, height = 5, speed = 20, family = a)