from django import forms
from .models import Visitee


class VisiteeForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Visitee

        # specify fields to be used
        fields = [
            "visitee_name",
            "visitee_status",
            "visitor_name"
        ]