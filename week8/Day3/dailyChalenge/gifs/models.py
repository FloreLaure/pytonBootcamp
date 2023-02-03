from django.db import models

# Create your models here.

class Gif(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField()
    uploader_name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class Category(models.Model):
	name = models.CharField(max_length=30)
	gif = models.ManyToManyField(Gif)

	def __str__(self):
		return f'{self.name}'



