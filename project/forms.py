
from django import forms
from .models import Blog

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=[
            'Title',
            'Date',
            'Description',
        ]   