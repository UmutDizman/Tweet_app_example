from django import forms

class AddTweetForm(forms.Form):
    name_input = forms.CharField(label='Name', max_length=50)
    massage_input = forms.CharField(label='Message',max_length=200)