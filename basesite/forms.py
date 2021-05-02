from django import forms

class Contact_form(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    contact_no = forms.CharField(required=False)
    message = forms.CharField(required=True, widget=forms.Textarea())
