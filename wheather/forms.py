from django import forms


class CityCheck(forms.Form):
    name = forms.CharField(label='City name', max_length=100)
    email = forms.EmailField(label='Email')

