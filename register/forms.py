from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=50, required=True, label="", widget=forms.TextInput(attrs={
		'placeholder' : 'Username',
		'style' : 'border : none; \
				   background-color: transparent;\
				   ::placeholder { \
					  color: red; \
					  opacity: 1; \
					}',
		'label' : 'Username',
				   }))
	first_name = forms.CharField(max_length = 254, required=True, label="", widget=forms.TextInput(attrs={
		'placeholder' : 'First Name',
		'style' : 'border : none; \
				   background-color: transparent;\'',
		}))
	email = forms.EmailField(max_length=254 ,required=True, label="", widget=forms.TextInput(attrs={
		'placeholder' : 'Email',
		'style' : 'border : none; \
				   background-color: transparent;\'',
		}))
	password1 = forms.CharField(max_length=100, required=True, label="", widget=forms.PasswordInput(attrs={
		'placeholder' : 'Password',
		'style' : 'border : none; \
				   background-color: transparent;\'',
		}))
	password2 = forms.CharField(max_length=100, required=True, label="", widget=forms.PasswordInput(attrs={
		'placeholder' : 'Re-enter Password',
		'style' : 'border : none; \
				   background-color: transparent;\'',
		}))