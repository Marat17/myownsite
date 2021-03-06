from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    post_text = models.CharField(max_length=140)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_text

# Create your models here.
