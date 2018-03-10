from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import formdata
def index(request):
	#return HttpResponse('hello world')
	query=formdata.objects.all()[:10]
	newone=formdata.objects.filter(name='yashwant',key='rtusucks').count()
	context={
		'formdata':query,
		'count':newone
	}
	return render(request,'index.html',context)

def signup(request):
	if (request.method=='POST'):
		name=request.POST['name']
		key=request.POST['key']
		query=formdata(name=name,key=key)
		query.save()
		return redirect('/dashboard')
	else:	
		return render(request,'index.html')

def login(request):
	#return HttpResponse('hello world')
	if (request.method=='POST'):
		name=request.POST['name']
		key=request.POST['key']
		query=formdata.objects.filter(name=name,key=key).count()
		if(query):
			return render(request,'dashboard.html')
		else:
			return render(request,'index.html')
	else:	
		return render(request,'index.html')

def dashboard(request):
	return HttpResponse('hello world')