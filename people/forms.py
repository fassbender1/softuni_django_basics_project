from django import forms
from django.utils import timezone

from people.mixin import SalaryValidationMixin
from people.models import Actor, Writer, Director


class ActorForm(SalaryValidationMixin, forms.ModelForm):
    MAX_SALARY = 50_000_000

    class Meta:
        model = Actor
        exclude = ['slug']
        labels = {
            'name': 'Actor Name',
            'salary': 'Salary USD)',
            'nationality': 'Country of Origin',
            'agent_email': 'Agent Contact Email',
            'birth_date': 'Birth Date',
        }

        error_messages = {
            'birth_date': {
                "invalid": "This Actor couldn't have been born in the future"
            }

        }

        help_texts = {
            "salary": "Maximum allowed salary: $50,000,000",
            "agent_email": "Spotlight and United Talent emails only",
        }

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter Actor's full name"}),
            "salary": forms.NumberInput(attrs={"placeholder": "ex: 20000000"}),
            "nationality": forms.TextInput(attrs={"placeholder": "ex: American"}),
            "agent_email": forms.EmailInput(attrs={"placeholder": "agent@spotlight.com, agent@unitedtalents.com..."}),
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }

        # def __init__(self):
        #     self.cleaned_data = None

        def clean_birth_date(self):
            birth_date = self.cleaned_data.get("birth_date")

            if birth_date and birth_date > timezone.now().date():
                raise forms.ValidationError("This Actor couldn't have been born in the future")

            return birth_date



class DirectorForm(SalaryValidationMixin, forms.ModelForm):
    MAX_SALARY = 15_000_000

    class Meta:
        model = Director
        exclude = ['slug']
        labels = {
            'name': 'Director Name',
            'salary': 'Salary USD',

        }

        help_texts = {
            "salary": "Maximum allowed salary: $15,000,000",
        }

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter the Director's full name"}),
            "salary": forms.NumberInput(attrs={"placeholder": "ex: 5000000"}),
        }



class WriterForm(SalaryValidationMixin, forms.ModelForm):
    MAX_SALARY = 5_000_000

    class Meta:
        model = Writer
        exclude = ['slug']
        labels = {
            'name': 'Writer Name',
            'salary': 'Salary USD',
        }

        help_texts = {
            "salary": "Maximum allowed salary: $5,000,000",
        }

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter the screenwriter's full name"}),
            "salary": forms.NumberInput(attrs={"placeholder": "ex: 1000000"}),
        }

