from Accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import Login_form_hai,Register_Form1,Change_password_form
# Create your views here.

def home(request):
    return render(request , 'home.html')



def Register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Register_Form1(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                upassword2 = form.cleaned_data['password2']

            try:
                if User.objects.filter(username = username).first():
                    messages.success(request, 'Username is taken.')
                    return redirect('/register')

                if User.objects.filter(email = email).first():
                    messages.success(request, 'Email is taken.')
                    return redirect('/register')
                
                user_obj = User(username = username , email = email)
                user_obj.set_password(password)
                user_obj.save()
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
                profile_obj.save()
                send_mail_after_registration(email , auth_token)
                return redirect('token_send')

            except Exception as e:
                print(e)
        else:
            form = Register_Form1()
        return render(request , 'register.html', {'form':form})

    else:
        return redirect('dashboard')


def Login(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = Login_form_hai(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user_obj = User.objects.filter(username = username).first()
                if user_obj is None:
                    messages.success(request, 'User not found.')
                    return redirect('/ogin')
                
                
                profile_obj = Profile.objects.filter(user = user_obj ).first()

                if not profile_obj.is_verified:
                    messages.success(request, 'Profile is not verified check your mail.')
                    return redirect('login')
                else:

                    user = authenticate(username = username , password = password)
                    if user is None:
                        messages.success(request, 'Wrong password.')
                        return redirect('login')
                    
                    login(request , user)
                    messages.success(request, 'Contrats!! You HAve Successfuly Logged in')
                    return redirect('dashboard')
        else:
            form = Login_form_hai()
        return render(request , 'login.html', {'form':form})
    else:
        return redirect('dashboard')

def Dashboard(request):
    return render(request, 'registration/dashboard.html')


def Logoutss(request):
    logout(request)
    messages.error(request, 'You Have Successfuly Logouts')
    return redirect('login')


def success(request):
    return render(request , 'success.html')

def token_send(request):
    return render(request , 'token_send.html')


def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/accounts/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')

def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    


def Change_Passwd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Change_password_form(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Contrats Password Changed Succesfuly')
                update_session_auth_hash(request, form.user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Password is not valid')
                return redirect('changepassword')
    
        else:
            form = Change_password_form(user=request.user)
            
        return render(request, 'accounts/changepasswd.html', {'form':form})

    else:
        return redirect('login')
       