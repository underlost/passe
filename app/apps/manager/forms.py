from django import forms
from .models import Entry, Category


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'url', 'username', 'password', 'comment', 'expires', 'category')
        widgets = {
            'title': forms.TextInput({'class': 'form-control', 'placeholder': 'Title'}),
            'url': forms.TextInput({'class': 'form-control', 'placeholder': 'Site URL'}),
            'username': forms.TextInput({'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.TextInput({'class': 'form-control', 'placeholder': 'Password'}),
            'comment': forms.Textarea({'class': 'form-control', 'placeholder': 'Additional comments here. Markdown supported.'}),
            'expires': forms.TextInput(attrs={'class': 'form-control datepicker'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'parent')
        widgets = {
            'parent': forms.Select({'class': 'form-control', 'placeholder': 'Parent Category (optional)'}),
            'title': forms.TextInput({'class': 'form-control', 'placeholder': 'Title'}),
        }
