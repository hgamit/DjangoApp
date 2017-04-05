from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.forms import formset_factory

from .forms import ArticleForm
from .models import Author

def get_name(request):
    # if this is a POST request we need to process the form data
    ArticleFormSet = formset_factory(ArticleForm, extra=2)
    formset = ArticleFormSet(request.POST or None)
    confirm_message = None
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        formset = ArticleFormSet(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            confirm_message = "Thanks for the input. We will get right back  to you"
            formset=None

    # if a GET (or any other method) we'll create a blank form
    else:
        formset = ArticleFormSet()

    context = {'formset':formset,'confirm_message':confirm_message,}
    template = 'name.html'
    return render(request,template,context)

def manage_authors(request):
    AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'))
    confirm_message = None
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            confirm_message = "Thanks for the input. We will get right back  to you"
            formset=None
            # do something.
    else:
        formset = AuthorFormSet()
    return render(request, 'name.html', {'formset': formset, 'confirm_message':confirm_message,})