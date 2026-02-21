from django import forms
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
            'duration_minutes': 'Enter the movie duration in minutes.',
        }
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Brief synopsis'}),
        }
        error_messages = {
            'budget': {
                'min_value': 'Budget must be positive.',
                'max_value': 'Budget cannot exceed $250 000 000.',
            }
        }

    def clean_budget(self):
        budget = self.cleaned_data.get('budget')
        if budget <= 0:
            raise ValidationError('The movie cannot have a negative budget.')
        return budget

    def clean_duration_minutes(self):
        duration = self.cleaned_data.get('duration')
        if 30 >= duration >= 300:
            raise ValidationError('Duration must be between 30 minutes and 300 minutes.')
        return duration

    def clean(self):
        cleaned_data = super().clean()
        release_date = cleaned_data.get('release_date')
        status = cleaned_data.get('status')
        if release_date and status == 'Pre-Production' or 'Post-Production' or 'Filming' and release_date < timezone.now().date():
            self.add_error('release_date', f"Movies that are in '{status}' state, cannot have a past release date.")

class DeleteConfirmationForm(forms.Form):
    confirm = forms.BooleanField(label="Check to confirm deletion")