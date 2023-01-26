from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label="First_name",max_length=100)
#     last_name = forms.CharField(label="Last_name",max_length=100)
#     email = forms.EmailField(label="Email")
#     review = forms.CharField(label="Please write your review here")

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        labels = {  
            'first_name':'Your first name:',
            'second_name':'Your second name:',
            'stars':'Rating:'
        }
        error_messages = {
            'stars': {
                'max_value':'Max value is 5',
                'min_value':'Min value is 1'
            }
        }