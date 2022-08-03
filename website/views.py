from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def About(request):
	return render(request, 'About.html')

def Projects(request):
	return render(request, 'Projects.html')

def Contact(request):
	return render(request, 'Contact.html')
