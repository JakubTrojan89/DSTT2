from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import LoginForm, RegisterForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
        return render(request, 'login_form.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('main')


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register_form.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return redirect('main')
        return render(request, 'register_form.html', {'form':form})