from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'annonce', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
            }),
            "annonce": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Anounce'
            }),
            "date": DateTimeInput(attrs={
                'class': "form-control",
                'placeholder': 'yy-mm-dd h:m:s'
            }),
            "full_text": Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Put content'
            }),
        }