from django import forms

class RegisterStaffForm(forms.Form):
    
    name = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    state = forms.CharField()
    city = forms.CharField()
    address = forms.CharField()
    phone_number = forms.IntegerField()