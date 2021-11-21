from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
        ]
        labels = {
            'title': 'Title',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
        }