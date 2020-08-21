from django import forms
from homepage.models import Joke

class AddJokeForm(forms.Form):
    JOKE_CHOICES = [
        (True, 'Roast'),
        (False, 'Boast')
    ]
    body = forms.CharField(max_length=280)
    joke_type = forms.ChoiceField(choices=JOKE_CHOICES, initial='', label='Joke Type')