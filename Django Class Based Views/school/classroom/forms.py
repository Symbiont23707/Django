from django import forms

class ContractForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)