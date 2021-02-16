from django import forms
from django.forms import fields

from .models import Article




class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =('headline','content','pub_date')
        widgets ={
            'headline': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(),
        }



