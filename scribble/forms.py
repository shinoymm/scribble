from django import forms


class CommentForm(forms.Form):
    commentator = forms.CharField(widget=forms.TextInput())
    commentator_mail = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

