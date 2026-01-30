from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return str(self.title)
    