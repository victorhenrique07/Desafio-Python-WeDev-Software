from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RegisterStaffForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
    
    name = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    state = forms.CharField()
    city = forms.CharField()
    address = forms.CharField()
    phone_number = forms.CharField()
    