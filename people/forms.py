from django import forms

from people.models import Actor


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'
        error_messages = {
            'name': {
                'unique': 'A person with this name already exists.'
            }
        }