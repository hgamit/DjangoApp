from django import forms
from dpickup.models import UserSearch

class UserSearchForm(forms.ModelForm):
    class Meta:
        model = UserSearch
        fields = (
            "search_adrs",
            "search_adrs_lat",
            "search_adrs_lng")
        widgets={
            "search_adrs":forms.TextInput(attrs={'placeholder':'Choose Region'}),
            "search_adrs_lat":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            "search_adrs_lng":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            }