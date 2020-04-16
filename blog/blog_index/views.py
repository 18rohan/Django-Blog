from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
	return render(request = request,
			template_name ='main/home.html',
			context = {'Blogs':Blog.objects.all()}
		)


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('main:index')
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])

	
	form = UserCreationForm
	return render(request,
				  'main/register.html',
				  context={'form':form}
		)
