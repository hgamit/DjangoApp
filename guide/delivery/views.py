from django.shortcuts import render, redirect, get_object_or_404
from delivery.models import UserDetail, UserSecurityInfo, UserAddress
from django.views.generic import UpdateView, DetailView, FormView, ListView, DeleteView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from delivery.forms import UserDetailForm, UserSecurityInfoForm, UserAddressForm
from django.urls import reverse_lazy
from django.conf import settings

@login_required
def new_userdetail(request):
    #if(get_object_or_404(UserDetail, customer=request.user)):
    if(False): 
        return redirect('boards:home')
    else:
        if request.method == 'POST':
            form = UserDetailForm(request.POST, request.FILES)
            if form.is_valid():
                detail = form.save(commit=False)
                detail.customer = request.user
                detail.save()
                return redirect('boards:home')
        else:
            form = UserDetailForm()
        return render(request, 'delivery/new_userdetail.html', {'form': form})

@login_required
def new_securityinfo(request):
    if(False):
    #if(get_object_or_404(UserSecurityInfo, customer=request.user)):
        return redirect('boards:home')
    else:
        if request.method == 'POST':
            form = UserSecurityInfoForm(request.POST, request.FILES)
            if form.is_valid():
                detail = form.save(commit=False)
                detail.customer = request.user
                detail.save()
                return redirect('delivery:display_securityinfo')
        else:
            form = UserSecurityInfoForm()
        return render(request, 'delivery/new_securityinfo.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class UserAddressCreateView(FormView):
    template_name = "delivery/new_useraddress.html"
    form_class = UserAddressForm
    success_url = reverse_lazy("delivery:display_useraddress")

    def form_valid(self, form):
        detail = form.save(commit=False)
        detail.customer = self.request.user
        detail.save()
        return super(UserAddressCreateView, self).form_valid(form)

    def get_object(self,queryset=None):
        return self.request.user.uaddress

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(UserAddressCreateView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['GMAPS'] = settings.GOOGLE_API_KEY
        return context

@method_decorator(login_required, name='dispatch')
class UserDetailUpdateView(UpdateView):
    model = UserDetail
    form_class = UserDetailForm
    template_name = 'delivery/edit_userdetail.html'
    success_url = reverse_lazy('delivery:display_userdetail')

    def get_object(self,queryset=None):
        return self.request.user.userprofile

@method_decorator(login_required, name='dispatch')
class UserSecurityInfoUpdateView(UpdateView):
    model = UserSecurityInfo
    form_class = UserSecurityInfoForm
    template_name = 'delivery/edit_securityinfo.html'
    success_url = reverse_lazy('delivery:display_securityinfo')

    def get_object(self,queryset=None):
        return self.request.user.usersecurity

@method_decorator(login_required, name='dispatch')
class UserAddressUpdateView(UpdateView):
    model = UserAddress
    form_class = UserAddressForm
    template_name = 'delivery/edit_useraddress.html'
    pk_url_kwarg = 'address_pk'
    context_object_name = 'address'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(customer=self.request.user)

    def form_valid(self, form):
        address = form.save(commit=False)
        address.last_updated = timezone.now()
        address.save()
        return redirect('delivery:display_useraddress')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(UserAddressUpdateView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['GMAPS'] = settings.GOOGLE_API_KEY
        return context

@method_decorator(login_required, name='dispatch')
class UserDetailDisplay(DetailView):
    model = UserDetail
    template_name = 'delivery/display_userdetail.html'

    def get_object(self,queryset=None):
        return self.request.user.userprofile

@method_decorator(login_required, name='dispatch')
class UserSecurityInfoDisplay(DetailView):
    model = UserSecurityInfo
    template_name = 'delivery/display_securityinfo.html'

    def get_object(self,queryset=None):
        return self.request.user.usersecurity

@method_decorator(login_required, name='dispatch')
class UserAddressDisplay(ListView):
    model = UserAddress
    queryset = UserAddress.objects.all() # querying DB
    template_name = 'delivery/display_useraddress.html'

    def get_object(self,queryset=None):
        return self.request.user.uaddress

@method_decorator(login_required, name='dispatch')
class UserAddressDeleteView(DeleteView):
    model = UserAddress
    template_name = 'delivery/delete_useraddress.html'
    success_url = reverse_lazy('delivery:display_useraddress')
    pk_url_kwarg = 'address_pk'
    context_object_name = 'address'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(customer=self.request.user)
