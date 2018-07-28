from django.contrib import admin
from blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
	fieldsets = [
	('The post', {'fields' : ['post_text']}),
	('Date of publication', {'fields': ['post_date']}),
	]

# Register your models here.
