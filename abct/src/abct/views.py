from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
	template = 'abct/home.html'
	return render(request,template,context)
	
def about(request):
	context = {}
	template = 'abct/about.html'
	return render(request,template,context)
