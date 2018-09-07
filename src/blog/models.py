from django.db import models
from django.conf import settings
import datetime
# Create your models here.\

class BlogPost(models.Model):
    title  = models.CharField(max_length=32)
    title_content = models.TextField()
    content = models.TextField()
    writter = models.CharField(max_length=32)
    mark = models.BooleanField(default=False)
    image = models.ImageField(null=True,blank=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
