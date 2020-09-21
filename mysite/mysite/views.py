from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
# from crypto.models import User
def index(request):
    return render(request, './crypto/index.html')


# def signupView(CreateView):
#     model = User
#     fields = ['username', 'email', 'password']
