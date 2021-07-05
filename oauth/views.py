from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import registerform, LoginForm

# Create your views here.
def home(response):
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    return render(response, "account/home.html", {"li":li})

def signup(response):
    if response.method == "POST":
        form = registerform(response.POST)
        if form.is_valid():
            form.save()
            return redirect("../login")
    else:
        form = registerform()
    return render(response, "account/signup.html", {'form':form})

def signout(response):
    logout(response)
    return redirect("http://127.0.0.1:8000")

# def signin(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request,user)
#         return redirect("../../")
#     else:
#         return render(request, "account/login.html")

def signin(response):
    form = LoginForm(response.POST or None)
    if response.POST and form.is_valid():
        user = form.login(response)
        if user:
            login(response, user)
            return HttpResponseRedirect("../../")# Redirect to a success page.
    return render(response, 'account/login.html', {'login_form': form })