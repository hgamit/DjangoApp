from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(label='Your title', max_length=100)
    pub_date = forms.DateField()