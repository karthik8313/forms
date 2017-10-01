from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import blogform2

def index(request):
	form=blogform2(request.POST)
	
	if form.is_valid():
		form.save()
	return render(request,'index.html',{'form':form})

def success(request):
	return HttpResponse("Form submitted successfully")