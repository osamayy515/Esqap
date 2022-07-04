from django import forms
from .models import Username

class UserForm(forms.ModelForm):
    class meta:
        models = Username
        fields = ['email', 'passwd']