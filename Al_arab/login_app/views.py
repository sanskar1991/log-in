from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random
import smtplib

from .forms import SignupForm, OTPVerifyForm
from .models import UserRegister


# Create your views here.
gmail_user = 'user3@gmail.com'
gmail_password = 'password'

def gen_otp():
    otp_num = random.randint(1000,9999)
    return otp_num

sent_otp = gen_otp()
print("1111111---Sent OTP : ", sent_otp)

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def register(request):
    if request.method == 'POST':
        print("222")
        form = SignupForm(request.POST)
        print("333")
        if form.is_valid():
            print("444")
            form.save(commit=False)
            print("555")
            return redirect('verify')
            if (verify_email(request, sent_otp)):
                print("121212")
                form.save()
                print("131313")
                return redirect('home')
            return HttpResponse("<h2>Invalid OTP!</h2>")
    else:
        print('1111')
        form = SignupForm()
    return render(request, 'register.html', {'form':form})




def verify_email(request):
    
    if request.method == 'POST':
        print("888")
        form = OTPVerifyForm(request.POST)
        print("999")
        if form.is_valid():
            print("10,10,10")
            otp_field = request.POST.get('otp')
            try:
                print("OOOTTTPPP:  ", otp_field, type(otp_field))
                print("222222---Sent OTP : ", sent_otp)
                if int(otp_field) == sent_otp:
                    print("011,011,011")
                    return redirect('home')
                print("012,012,012")
                return HttpResponse("<h3>Invalid OTP HERE!</h3>")
            except:
                return HttpResponse("<h3>Exception raised here!</h3>")
            print("11,11,11")
    else:
        print("666")
        email(sent_otp)
        form = OTPVerifyForm()
        print("777")
    return render(request, 'verification.html', {'form':form})




def email(sent_otp):
    
    sent_from = gmail_user
    to = ['user1@gmail.com','user2@gmail.com']
    subject = 'Demo Mail'
    message = f"""Hi Pratiksha,\n \
    This email is to inform you that the email verification you wanted for the login page is working now. This is a demo mail to test the email verification functionality.\n \
    Your code is {sent_otp}. \n \
    Please send this code to me.\n\n \
    Thanks and Regards\n \
    Hello World"""
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = 
    # send_mail( subject, message, email_from, recipient_list )

    try:
        print("aaaa")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        print("bbbb")
        server.ehlo()
        print("cccc")
        server.login(gmail_user, gmail_password)
        print("dddd")
        server.sendmail()
        print("eeee")
        server.close()
        print("ffff")

        print('Email sent!')
    except:
        server.login(gmail_user, gmail_password)
        print('Something went wrong...')