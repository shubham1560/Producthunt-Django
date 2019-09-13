from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def login(request):
    if request.method=='POST':
        print("Post Method")
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'Login.html', {'error': 'username or password is incorrect'})
            print("User not found")

        # return render(request, 'SignUp.html')
    else:
        return render(request, 'Login.html')


def signup(request):
    # print("-------------------")
    print(request.POST)
    # print(request.POST["username"])
    # print(request.POST["password1"])
    # print(request.POST["password2"])
    # print("-------------------")
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            print("Inside If")
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'SignUp.html', {"error":"User name has already been taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'SignUp.html', {"error": "User name has already been taken"})

    else:
        return render(request, "SignUp.html")


def logout(request):
    return render(request, "Logout.html")