from django import forms
from dmanage.models import UserPackage

class UserPackageForm(forms.ModelForm):
    class Meta:
        model = UserPackage
        fields = (
            "pickup_adrs",
            "delivery_adrs",
            "package_type", 
            "package_description", 
            "package_weight", 
            "package_dimensions", 
            "package_value", 
            "delivery_timeline", 
            "driving_distance", 
            "bicycling_distance", 
            "transit_distance", 
            "driving_duration", 
            "bicycling_duration", 
            "transit_duration")
        widgets={
            "package_description":forms.TextInput(attrs={'placeholder':'It contains fragile item.'}),
            "package_weight":forms.NumberInput(attrs={'placeholder':'Approx. weight below 30 pounds', 'min' : '0'}),  
            "package_value":forms.NumberInput(attrs={'placeholder':'Below $5000', 'min' : '0'}),
            "driving_distance":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            "bicycling_distance":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            "transit_distance":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            "driving_duration":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            "bicycling_duration":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            "transit_duration":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            }