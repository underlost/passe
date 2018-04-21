from django import forms
from .models import Entry, Category


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'url', 'username', 'password', 'comment', 'expires', 'category')
        widgets = {
            'expires': forms.TextInput(attrs={'class': 'datepicker'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'parent')
        widgets = {
            'parent': forms.Select({'class': 'form-control', 'placeholder': 'Parent Category (optional)'}),
            'title': forms.TextInput({'class': 'form-control', 'placeholder': 'Title'})
        }
