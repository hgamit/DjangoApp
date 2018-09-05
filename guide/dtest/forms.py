from django import forms
from dtest.models import TestPackage, Package

class TestPackageForm(forms.ModelForm):
    class Meta:
        model = TestPackage
        fields = (
            "package_description",
            "package_descriptionhid")
        widgets={
            "package_description":forms.TextInput(attrs={'placeholder':'It contains fragile item.'}),
            "package_descriptionhid":forms.TextInput(attrs={'type':'hidden'}),
            }

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = (
            "pickup_adrs",
            "delivery_adrs",
            "package_type", 
            "package_description", 
            "package_weight", 
            "package_dimensions", 
            "package_value", 
            "delivery_timeline", 
            #"driving_distance", 
            # "bicycling_distance", 
            # "transit_distance", 
            "driving_duration", )
            # "bicycling_duration", 
            # "transit_duration")
        widgets={
            "package_description":forms.TextInput(attrs={'placeholder':'It contains fragile item.'}),
            "package_weight":forms.TextInput(attrs={'placeholder':'Approx. weight below 30 pounds'}),  
            "package_value":forms.TextInput(attrs={'placeholder':'Below $5000'}),
            #"driving_distance":forms.TextInput(attrs={'type':'hidden'}),
            # "bicycling_distance":forms.TextInput(attrs={'type':'hidden'}),
            # "transit_distance":forms.TextInput(attrs={'type':'hidden'}),
            "driving_duration":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            # "bicycling_duration":forms.TextInput(attrs={'type':'hidden'}),
            # "transit_duration":forms.TextInput(attrs={'type':'hidden'}),
            }