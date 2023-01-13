from django import forms
from main import models


class Registration(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ('__all__')