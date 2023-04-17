from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from .models import CovidiaAppUser
from django.core.files.storage import FileSystemStorage


def SignIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('Welcome')
            
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('SignIn')

    else:
        return render(request,'SignIn.html')

   


def SignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1'] 
        password2 = request.POST['password2']
        if username == False:
            messages.info(request,'Username Required')

        if password1 == password2:
            if CovidiaAppUser.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect("SignUp")
            elif CovidiaAppUser.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect("SignUp")
            else:
                user = CovidiaAppUser.objects.create_user(username = username, email = email, password = password1)
                user.save(); 
                messages.info(request,"User Created")
                return redirect("SignIn")

        else:
            messages.info(request, 'Password not matched..')
            return redirect("SignUp")
    else:
        return render(request, 'SignUp.html')
    


def Welcome(request):
    return render(request, 'Welcome.html')

def CovidiaTest(request):
    return render(request,'Covidia.html')

def SignOut(request):
    logout(request)
    messages.success(request, 'Logged out successfully !')
    return redirect('SignIn')