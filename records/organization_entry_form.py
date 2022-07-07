from django import forms
from .models import Organization


class OrganizationForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Organization

        # specify fields to be used
        fields = [
            "organization_name",
            "mobile_number"
        ]
