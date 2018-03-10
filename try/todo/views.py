from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse('yashwant')

def home():
	context=locals()
	template='home.html'
	return render(request,template,context)