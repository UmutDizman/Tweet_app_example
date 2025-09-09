from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet


class AddTweetForm(forms.Form):
    name_input = forms.CharField(label='Name', max_length=50)
    massage_input = forms.CharField(label='Message',max_length=200,
                                    widget=forms.Textarea(attrs={"class":"tweetmassege"}))
    


class AddtweetModelForm(ModelForm):
        class Meta:
            model = Tweet
            fields = ['username','massage']