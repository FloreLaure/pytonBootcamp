from django import forms
from .models import Category

class TodoForm(forms.Form):
    title = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'placeholder': 'Write your name'
                })
            )

    uploader_name = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'placeholder': 'Write your name'
                })
            )

    date_completion = forms.DateField(label="",input_formats=['%d/%m/%Y'],required=False,widget= forms.TextInput(attrs={'placeholder':'31/12/2000'}))
    deadline_date = forms.DateField(label="",input_formats=['%d/%m/%Y'],required=False,widget= forms.TextInput(attrs={'placeholder':'31/12/2000'}))


    title = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'placeholder': 'Write the title'
                })
            )
    url = forms.URLField()
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    has_been_done = forms.BooleanField()

