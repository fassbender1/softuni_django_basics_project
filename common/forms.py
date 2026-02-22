from django import forms

class SearchForm(forms.Form):
    search_name = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Search...',
            'class': 'form-control',
        })
    )