from django import forms

class RomanForm(forms.Form):
    integer = forms.IntegerField(min_value=1, max_value=3999)
