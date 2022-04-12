from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=20, label='First Name')
    last_name = forms.CharField(max_length=10, label='Last Name')
    age = forms.IntegerField(label='Age')
    stuid = forms.IntegerField(label='Student ID')