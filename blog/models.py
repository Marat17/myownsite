from django.db import models

class BlogPost(models.Model):
	post_text = models.CharField(max_length=140)
	post_date = models.DateTimeField('date published')

# Create your models here.
