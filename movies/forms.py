from django import forms

from common.choices import MovieStatusChoices
from movies.models import Movie
from django.core.exceptions import ValidationError
from django.utils import timezone

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['slug']
        labels = {
            'title': 'Movie Title',
            'release_date': 'Release Date',
            'budget': 'Budget (USD)',
        }
        help_texts = {
            'status': 'Select the current movie production stage.',
        }

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Brief synopsis'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            "release_date": forms.DateInput(attrs={"type": "date"}),
            "actors": forms.SelectMultiple(attrs={"class": "form-select"}),
            "directors": forms.SelectMultiple(attrs={"class": "form-select"}),
            "writers": forms.SelectMultiple(attrs={"class": "form-select"}),
            "studio": forms.Select(attrs={"class": "form-select"}),
        }
        error_messages = {
            'budget': {
                'min_value': 'Budget must be positive.',
                'max_value': 'Budget cannot exceed $250 000 000.',
            },
            'duration': {
                'placeholder': 'Duration in minutes.',
            },
            'release_date': {
                'required': "The release date is required.",
            }
        }

    def clean_budget(self):
        budget = self.cleaned_data.get('budget')
        max_budget = 250000000
        if budget > max_budget:
            raise ValidationError('Budget cannot exceed $250 000 000.')
        if budget <= 0:
            raise ValidationError('The movie cannot have a negative budget.')
        return budget

    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if not (30 <= duration <= 300):
            raise ValidationError('Duration must be between 30 and 300 minutes.')
        return duration

    def clean(self):
        cleaned_data = super().clean()
        release_date = cleaned_data.get('release_date')
        status = cleaned_data.get('status')

        restricted_statuses = {
            MovieStatusChoices.Pre_Production,
            MovieStatusChoices.Filming,
            MovieStatusChoices.Post_Production,
        }

        if release_date and status in restricted_statuses:
            if release_date < timezone.now().date():
                self.add_error(
                    'release_date',
                    f"Movies in '{MovieStatusChoices(status).label}' state cannot have a past release date."
                )
        return cleaned_data

class MovieDeleteForm(MovieForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True

class DeleteConfirmationForm(forms.Form):
    confirm = forms.BooleanField(label="Check to confirm deletion")