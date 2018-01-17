from django import forms
from . models import ID


class UserForm(forms.Form):
    password=forms.CharField(widget=forms.PasswordInput)
    your_name = forms.CharField(label='Your name', max_length=100)

    #class Meta:
     #   model = ID
      #  fields = ('username','password')