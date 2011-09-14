# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

#import from User
from django.contrib.auth.models import User

#import from app's models
from loggin.models import SignupForm,userinfo

#other imports
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

def home(request):
	return render_to_response('loggin/home.html',{'lol': request.user })

def signin(request):
	if request.user.is_authenticated():
		return render_to_response('loggin/alert.html',{'user':request.user})
	error_message=""
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/loggin/')
			else:
				error_message = "Sorry!your account is diabled"
		else:
			error_message="Username/Password don't match"
	return render_to_response('loggin/signin.html',{'error_message':error_message},context_instance=RequestContext(request))

def signout(request):
	logout(request)
	return HttpResponseRedirect('/loggin/')

def signup(request):
	if request.user.is_authenticated():
		return render_to_response('loggin/alert.html',{'user':request.user})
	if request.method == 'POST':
		form=SignupForm(request.POST)   #a bound form
		if form.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			first_name=form.cleaned_data['first_name']
			last_name=form.cleaned_data['last_name']
			age=form.cleaned_data['age']
			country=form.cleaned_data['country']
			email=form.cleaned_data['email']
			newuser=User.objects.create_user(
											username,
											email,
										    password
			                           )
			newuser_details=userinfo.objects.create(
														country=country,
														age=age,
														user=newuser
													)
			newuser.first_name=first_name
			newuser.last_name=last_name
			newuser.save()
			newuser_details.save()
			return HttpResponseRedirect('/loggin/thanks/')
	else:
		form=SignupForm()

	return render_to_response('loggin/signup.html',{'form':form},context_instance=RequestContext(request))

def thanks(request):
	return render_to_response('loggin/thanks.html',{})
