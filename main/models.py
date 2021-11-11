from django.db import models

# Create your models here.
from django.db import models

from account.models import User


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=200)
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.name}'
        else:
            return self.name

    def get_children(self):
        if self.children:
            return self.children.all()
        return False

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='places')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='places')
    created = models.DateTimeField()

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='posts')
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
        
