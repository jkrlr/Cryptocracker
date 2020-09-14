from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView

def index(request):
    return render(request, './crypto/index.html')


def signupView(CreateView):
    model = Users
    fields = ['username', 'email', 'password']