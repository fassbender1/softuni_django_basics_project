from django import forms
from django.utils import timezone
from studios.models import Studio


class StudioForm(forms.ModelForm):

    class Meta:
        model = Studio
        exclude = ["slug"]
        labels = {
            "name": "Studio Name",
            "location": "Studio Set Location",
            "founded_in": "Founded On",
            "studio_head": "Studio Head",
        }
        help_texts = {
            "name": "Studio name must be unique.",
            "founded_in": "Cannot be a future date.",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "ex: Warner Bros"}),
            "location": forms.TextInput(attrs={"placeholder": "ex: Los Angeles, USA"}),
            "founded_in": forms.DateInput(attrs={"type": "date"}),
            "studio_head": forms.TextInput(attrs={"placeholder": "CEO/Chairman name"}),
        }

    def clean_founded_in(self):
        founded_in = self.cleaned_data.get("founded_in")

        if founded_in and founded_in > timezone.now().date():
            raise forms.ValidationError(
                "Founded date cannot be in the future."
            )

        return founded_in

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if Studio.objects.filter(name__iexact=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("There is already a registered studio with this name.")

        return name