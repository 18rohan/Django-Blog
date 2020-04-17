from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.

def index(request):
	return render(request = request,
			template_name ='main/home.html',
			context = {'Blogs':Blog.objects.all()}
		)


def register(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.info(request, f"New account created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect('main:index')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
			return render(request = request,
						  template_name='main/register.html',
						  context = {"form":form}
						)

	
	form = NewUserForm
	return render(request,
				  'main/register.html',
				  context={'form':form}
		)

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect('main:index')

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('main:index')
			else:
				messages.error(request, "Invalid username or password")
		else:
				messages.error(request, "Invalid username or password")	
	form =AuthenticationForm()
	return render(request,
				'main/login.html',
				{'form':form}
		)
