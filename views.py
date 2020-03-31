from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from main.models import *



def login(request):

    if request.method == "POST":
        usrname = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=usrname, password=password)

        if user is not None:
            auth.login(request, user)
            //session User save
            return redirect("/")
        else:
            messages.info(request, 'Enter correct username and password')
            return redirect('/accounts/login')

    else:
        return render(request, 'accounts/login.html')






def signup(request):

    if request.method == "POST":
        first_name = request.POST.get('first')
        last_name = request.POST.get('last')
        usrname = request.POST.get('usern')
        password1 = request.POST.get('password')
        password2 = request.POST.get('cpassword')
        email = request.POST.get('email')

        if User.objects.filter(username=usrname).exists():
            messages.info(request, 'username taken')
            return redirect('/accounts/signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'email-id taken')
            return redirect('/accounts/signup')
        else:

            usr = User.objects.create_user(username=usrname, password=password1, email=email, first_name=first_name, last_name=last_name)
            usr.save()
            return redirect('/accounts/login')

    else:
        return render(request, 'accounts/signup.html')



def logout(request):
    HouseDetails.objects.all().delete()
    // session remove user
    auth.logout(request)
    return redirect('/')
