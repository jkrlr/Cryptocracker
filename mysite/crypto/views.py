from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .decorators import login_required
from quiz.forms import ContestForm
from .forms import SinupForm

# from django.contrib import message
# from .forms import SinupForm


# from django.views.decorators.cache import cache_control
login_error = 0


def base(request):
    print("base")
    return render(request, 'crypto/base.html')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)


@login_required
def index(request, uname):
    print("index")
    print(uname, "asda")
    profile = Profile.objects.get(user=request.user)
    return render(request, 'crypto/index.html', {'profile': profile})


@login_required
def make_admin(request):
    user = request.user
    if user.is_superuser:
        all_users = Profile.objects.all()
        profile = Profile.objects.get(user=request.user)
        return render(request, 'crypto/make_admin.html', {'users': all_users, 'profile': profile})
    else:
        messages.error(request, "You are not a super user!!")
        return redirect('/')


@login_required
def admin_form(request):
    adminlist = request.POST.getlist('isadmin')
    for u in adminlist:
        u = int(u.encode('ascii', 'ignore'))
        user = User.objects.get(pk=u)
        print(user.username)
        profile = Profile.objects.get(user=user)
        if profile.is_admin:
            profile.is_admin = False
        else:
            profile.is_admin = True
        profile.save()
    return redirect('/make_admin/')




# def signup(request):
#     if request.method == 'POST':
#         form = SinupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get('username')
#             name = form.cleaned_data.get('name')

#             fname, lname = name.split(' ')
#             fname = fname.title()
#             lname = lname.title()

#             user = User(username=username, password=form.cleaned_data.get('password'),
#                         email=form.cleaned_data.get('email'), first_name=fname, last_name=lname)
#             user.set_password(form.cleaned_data.get('password'))
#             user.save()
#             profile = Profile(user=user, roll=form.cleaned_data.get('roll'), phone=form.cleaned_data.get('phone'))
#             profile.save()
#     return redirect('/')









# def signup(request):
#     if request.method == 'POST':
#         form = SinupForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             profile = form.save()
#             profile.user = user
#             profile.save()

#             # print(request.POST.get('username'), "l")
#             # name = request.POST.get('name')
#             # fname, lname = name.split(' ')
#             # fname = fname.title()
#             # lname = lname.title()
#             # user = User(username=request.POST['username'], password=request.POST['password'],
#             #             email=request.POST['email'], first_name=fname, last_name=lname)
#             # user.set_password(request.POST['password'])
#             # user.save()
#             # profile = Profile(
#             #     user=user, roll=request.POST['roll'], phone=request.POST['phone'])
#             # profile.save()
#             return redirect('/')

def signup(request):
    if request.method == 'POST':
        print(request.POST.get('username'), "l")
        
        name=request.POST.get('name')
        fname,lname=name.split(' ')
        fname=fname.title()
        lname=lname.title()
        user=User(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'],first_name=fname,last_name=lname)
        user.set_password(request.POST['password'])
        user.save()
        profile=Profile(user=user,roll_no=request.POST['roll_no'],phone_no=request.POST['phone_no'])
        profile.save()
        return redirect('/')



def loginm(request):
    print("1")
    print(request.POST.get('username'), request.POST.get('password'))
    try:
        user = User.objects.get(username=request.POST.get('username'))
    except:
        error_msg = "Wrong credentials"
        messages.error(request, error_msg)
        return redirect('/')
    print(user.username, user.password)
    user = authenticate(request, username=user.username,
                        password=request.POST.get('password'))
    print(user)
    if user is not None:
        login(request, user)
        return redirect('/'+user.username+'/')
    else:
        print("Wrong")
        return redirect('/')


@login_required
def logoutm(request):
    logout(request)
    return redirect('/')
