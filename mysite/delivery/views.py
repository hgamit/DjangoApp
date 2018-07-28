from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserDetailForm, DocumentForm
from .models import UserDetail
from django.views.generic import UpdateView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'delivery/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'delivery/simple_upload.html')

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            details = form.save(commit=False)
            details.customer = request.user
            details.save()
            return redirect('boards:home')
    else:
        form = DocumentForm()
    return render(request, 'delivery/model_form_upload.html', {
        'form': form
    })

def getdetails(request):
    #user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = UserDetailForm(request.POST, request.FILES)
        if form.is_valid():
            details = form.save(commit=False)
            details.customer = request.user
            details.save()
            return redirect('boards:home')  # TODO: redirect to the home page
    else:
        form = UserDetailForm()
    return render(request, 'delivery/userdetails.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class UserUpdateDetail(UpdateView):
    model = UserDetail
    fields = ('first_name', 'last_name', 'sex', 'date_of_birth', 'user_pic' )
    template_name = 'delivery/my_details.html'
    success_url = reverse_lazy('delivery:showdetails')

    def get_object(self):
        return self.request.user.userdetail

def user_details(request):
    return render(request, 'delivery/showdetails.html', {'request': request})

