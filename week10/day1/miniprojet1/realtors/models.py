from django.db import models
from datetime import datetime
# Create your models here.

class Realtor(models.Model):

    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def str(self):
        return self.name