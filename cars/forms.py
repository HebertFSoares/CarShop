from django import forms

class CarFrom(forms.Form):
     model = forms.CharField(max_length=200)