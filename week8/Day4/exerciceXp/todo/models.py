from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=30)
	url = models.URLField()


	def __str__(self):
		return f'{self.name}'

class Todo(models.Model):
    title = models.CharField(max_length=30)
    has_been_done = models.BooleanField(default=False)
    uploader_name = models.CharField(max_length=30)
    date_creation = models.DateField()
    date_completion = models.DateField()
    deadline_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'



