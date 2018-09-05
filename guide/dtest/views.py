from django.shortcuts import render, redirect, get_object_or_404
from dtest.models import TestPackage, Package
from django.views.generic import UpdateView, DetailView, FormView, ListView, DeleteView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dtest.forms import TestPackageForm, PackageForm
from django.urls import reverse_lazy

# Create your views here.
@method_decorator(login_required, name='dispatch')
class TestPackageCreateView(FormView):
    template_name = "dtest/new_testpackage.html"
    form_class = TestPackageForm
    success_url = reverse_lazy("boards:home")

    def form_valid(self, form):
        detail = form.save(commit=False)
        detail.customer = self.request.user
        package_description = form.cleaned_data['package_description']
        package_descriptionhid = form.cleaned_data['package_descriptionhid']
        
        charge = 5.0
        if package_descriptionhid and package_description:
            charge += 10
        detail.package_descriptionplus = charge
        detail.save()
        print (charge)
        return super(TestPackageCreateView, self).form_valid(form)

    def get_object(self,queryset=None):
        return self.request.user.testpackage


# Create your views here.
@method_decorator(login_required, name='dispatch')
class PackageCreateView(FormView):
    template_name = "dtest/new_package.html"
    form_class = PackageForm
    success_url = reverse_lazy("boards:home")

    def form_valid(self, form):
        detail = form.save(commit=False)
        detail.customer = self.request.user
        #driving_distance = form.cleaned_data['driving_distance']
        driving_duration = form.cleaned_data['driving_duration']
        package_dimensions = form.cleaned_data['package_dimensions']
        delivery_timeline = form.cleaned_data['delivery_timeline']
        
        charge = 5.0
        # if driving_distance > 50 and 4<driving_duration<24 and delivery_timeline == "Same day Delivery(24x1)":
        #     charge += 10
        # elif driving_distance > 50 and driving_duration>24:
        #     charge += 5
        # else:
        #     if (package_dimensions == "Small (Under 15 x 12 x 1)" or package_dimensions == "Medium (Under 15 x 12 x 6)") and (delivery_timeline == "Within 2 Hours" or delivery_timeline == "Within 2 Hours"):
        #         charge += 10
        #     elif package_dimensions == "Large (Under 24 x 12 x 6)" and (delivery_timeline == "Within 2 Hours" or delivery_timeline == "Within 2 Hours"):
        #         charge += 12
        #     elif delivery_timeline== "Same day Delivery(24x1)":
        #         charge += 8
        #     else:
        #         charge += 5

        detail.shipping_charge = charge
        detail.save()
        print (charge)
        return super(PackageCreateView, self).form_valid(form)

    def get_object(self,queryset=None):
        return self.request.user.userpackage
