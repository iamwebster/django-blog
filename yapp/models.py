from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
