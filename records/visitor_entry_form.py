from django import forms
from .models import Visitor


class VisitorsForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Visitor

        # specify fields to be used
        fields = [
            "visitor_name",
            "phone_number",
            "id_or_passport",
            "organization",
            "visitee",
            "time_in",
            "time_out"
        ]