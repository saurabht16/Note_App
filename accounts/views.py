from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']
            User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
            return HttpResponseRedirect("/login/")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
