from django.forms import ModelForm
from .models import Vote
from django import forms


class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['name', 'presence', 'drink']

        widgets = {
            'presence': forms.CheckboxSelectMultiple(),
            'drink': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
