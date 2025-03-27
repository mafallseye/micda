from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def login_blog(request):
    if request.method=="POST":
        username= request.POST['username']
        pwd= request.POST['pwd']
        user=authenticate(username=username,password=pwd)
        if user is not None:
            return redirect("/admin")
        else:
            messages.error(request,'Erreur authentification')
            return render(request,'login.html')
        print(username)
        print(pwd)
    return render(request,'login.html')
