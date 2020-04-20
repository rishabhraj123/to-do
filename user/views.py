from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("HELLO")
            print(form)
            form.save()
        return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "user/register.html", {"form":form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.error(request, f'something went wrong!')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
