from django import forms

from people.models import Actor, Writer, Director


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        exclude = ['slug']
        labels = {
            'name': 'Actor Name',
            'salary': 'Salary',
            'nationality': 'Born in',
            'agent_email': 'Agent Contact Info',
        }
        error_messages = {
            'name': {
                'unique': 'A person with this name already exists.'
            },
            'salary': {
                'max_value': "An Actor's salary cannot exceed $50,000,000"
            }
        }

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        exclude = ['slug']
        labes = {
            'name': 'Director Name',
            'salary': 'Salary',

        }

        error_messages = {
            'salary': {
                'max_value': "A Director's salary cannot exceed $15,000,000"
            }
        }

class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        exclude = ['slug']
        labes = {
            'name': 'Writer Name',
            'salary': 'Salary',
        }

        error_messages = {
            'salary': {
                'max_value': "A Writer's salary cannot exceed $5,000,000"
            }
        }