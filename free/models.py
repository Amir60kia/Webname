from django.db import models

# Create your models here.
class Free (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    images= models.ImageField(default='default.jpg',blank=True)
    #addin author
    def __str__ (self):
        return self.title
    def snippet(self):
        return self.body[0:50]+'...'
