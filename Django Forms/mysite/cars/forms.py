from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label="First_name",max_length=100)
    last_name = forms.CharField(label="Last_name",max_length=100)
    email = forms.EmailField(label="Email")
    review = forms.CharField(label="Please write your review here")
