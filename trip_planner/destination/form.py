from django import forms

class CityForm(forms.Form):
    destination_city = forms.CharField(label='Your trip destination', max_length=100)