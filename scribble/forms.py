from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.Form):
    commentator = forms.CharField(widget=forms.TextInput())
    commentator_mail = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

