from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'Login.html')


def signUp(request):
    return render(request, "SignUp.html")


def logout(request):
    return render(request, "Logout.html")