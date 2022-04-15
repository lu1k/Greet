from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import RegisterForm

# Create your views here.
def register(response):
	if response.method == 'POST':
		form = RegisterForm(response.POST)

		if form.is_valid():
			username = form.cleaned_data['username'].lower()
			first_name = form.cleaned_data['first_name']
			email = form.cleaned_data['email']
			password1 = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']

			if password1 == password2:
				if User.objects.filter(username=username).exists():
					print("Username not available!")
				else : 
					user = User.objects.create_user(
						username=username, 
						first_name=first_name, 
						email=email, 
						password=password1, 
						is_active=True
						)
					print("User created successfully")

				return redirect('/')

	else :
		form = RegisterForm()

	return render(response, 'register/register.html', {"form" : form})