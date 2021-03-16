from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def register(request):
    return HttpResponse('<h1>Register Page</h1>')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             email()
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

def email(request):
    subject = 'Demo Mail'
    message = 'This is a demo mail to test the email verification functionality. Your code is 3344. '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sanskarj123@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('redirect to a new page')
