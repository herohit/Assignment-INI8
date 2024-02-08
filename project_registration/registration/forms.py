from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        exclude = ['ID']
        help_texts = {'DateOfBirth': 'Please enter your date of birth in the format: MM/DD/YYYY',}
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
