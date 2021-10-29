from django import forms
from django.contrib.auth.models  import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.forms import UsernameField

class Register_Form1(UserCreationForm):
    password1 = forms.CharField( label='Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Your password here'}),required=True)
    password2 = forms.CharField( label='Confrim Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm your password here'}))
    username = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'})) 
    email = forms.CharField( widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your E-Mail here'})) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Login_form_hai(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Username', 'autofocus':True}))
    password = forms.CharField( strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password', 'autocomplete':'current-password' }))


class Change_password_form(PasswordChangeForm):
    old_password = forms.CharField( strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Old Password', 'autocomplete':'current-password' }),required=True)
    new_password1 = forms.CharField(label='New Password', strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter New Password', 'autocomplete':'current-password' }),required=True)
    new_password2 = forms.CharField(label='Confirm Password', strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Confirm Password', 'autocomplete':'current-password' }),required=True)

class Reset_Password_form2(PasswordResetForm):
    email = forms.CharField( widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter registerd email id  here'})) 

class Set_Password_form2(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter New Password', 'autocomplete':'current-password' }),required=True)
    new_password2 = forms.CharField(label='Confirm Password', strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Confirm Password', 'autocomplete':'current-password' }),required=True)

