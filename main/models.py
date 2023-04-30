from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Article(models.Model):
    name=  models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    content= models.TextField()

    author= models.ManyToManyField('Author')

    def __str__(self):
        return self.name