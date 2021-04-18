from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DetailView, FormView, ListView, CreateView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from math import radians, cos, sin, asin, sqrt

from django.template.loader import render_to_string
from django.http import JsonResponse
from django.conf import settings

from dmanage.models import UserPackage
from delivery.models import UserAddress
from dpickup.forms import UserSearchForm

# Create your views here.
@method_decorator(login_required, name='dispatch')
class UserSearchCreateView(CreateView):
    template_name = "dpickup/packagenearby.html"
    form_class = UserSearchForm
    success_url = reverse_lazy("boards:home")
    data = dict()
    #context_object_name = 'distances'

    def form_valid(self, form):
        detail = form.save(commit=False)
        detail.customer = self.request.user
        search_adrs_lat = form.cleaned_data['search_adrs_lat']
        search_adrs_lng = form.cleaned_data['search_adrs_lng']
        detail.save()

        self.data['form_is_valid'] = True
        distances = UserPackage.objects.with_distance(search_adrs_lat, search_adrs_lng)
        self.data['html_packages_list'] = render_to_string('dpickup/includes/partial_packages_list.html', {
                'distances': distances
            })

        if detail is not None:
            return JsonResponse(self.data)
        else:
            return super(UserSearchCreateView, self).form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user.usersearch

    def get_context_data(self, **kwargs):
        context = super(UserSearchCreateView, self).get_context_data(**kwargs)
        point = UserAddress()
        lattitude = point.get_permanent_lat()
        longitude = point.get_permanent_lng()
        context['distances'] = UserPackage.objects.with_distance(lattitude, longitude)
        context['GMAPS'] = settings.GOOGLE_API_KEY
        return context

""" def packages_nearby(request):
    point = UserAddress()
    form = UserSearchForm()
    lattitude = point.get_permanent_lat()
    longitude = point.get_permanent_lng()
    distances = UserPackage.objects.with_distance(lattitude, longitude)
    return render(request, 'dpickup/packagenearby.html', {'distances': distances, 'form': form})

@login_required
def packages_search(request):

    data = dict()

    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.customer = request.user
            search_adrs_lat = form.cleaned_data['search_adrs_lat']
            search_adrs_lng = form.cleaned_data['search_adrs_lng']
            detail.save()

            data['form_is_valid'] = True
            distances = UserPackage.objects.with_distance(search_adrs_lat, search_adrs_lng)
            data['html_packages_list'] = render_to_string('dpickup/includes/partial_packages_list.html', {
                'distances': distances
            })

        else:
            data['form_is_valid'] = False
    else:
        form = UserSearchForm()

    context = {'form': form, 'GMAPS' : settings.GOOGLE_API_KEY}
    data['html_form'] = render_to_string('dpickup/includes/partial_packages_search.html',
        context,
        request=request,
    )
    return JsonResponse(data) """