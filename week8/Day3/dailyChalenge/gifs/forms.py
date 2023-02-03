from django import forms
from .models import Category

class GifForm(forms.Form):
    uploader_name = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'placeholder': 'Write your name'
                })
            )

    title = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'placeholder': 'Write the title'
                })
            )
    url = forms.URLField()
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

class CategoryForm(forms.Form):
	name = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'placeholder': 'Write the name of category'
                })
            )
