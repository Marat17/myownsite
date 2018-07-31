from django import forms
from .models import BlogPost
from django.utils import timezone


class CreateNewPost(forms.ModelForm):
    post_text = forms.CharField(max_length=140, help_text='Please type your new post here:', widget=forms.Textarea)
    
    class Meta:
        model = BlogPost
        fields = ('post_text',)