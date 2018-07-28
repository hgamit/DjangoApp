from django import forms
from .models import UserDetail, Document

class UserDetailForm(forms.ModelForm):
    #message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = UserDetail
        fields = ['first_name', 'last_name', 'sex', 'date_of_birth', 'user_pic' ]

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )