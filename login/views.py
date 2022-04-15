from django.shortcuts import render
from django.contrib import auth

# Create your views here.
def login(response):
	return render(response, 'login/login.html', {})