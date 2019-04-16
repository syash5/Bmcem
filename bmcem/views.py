from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from .forms import UserRegistrationForm
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import (authenticate,
                                 login,
                                 logout
                                 )
# Create your views here.


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        title = "Create an Account"
        form = UserRegistrationForm(
            request.POST or None,
            request.FILES or None
            )

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)

            return HttpResponseRedirect(reverse('index'))

        context = {"title": title, "form": form}

        return render(request, "bmcem/form.html", context)

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "accounts/login.html", context)
    else:
        return render(request, "bmcem/login.html", context)


def index(request):
    return render(request, 'bmcem/index.html')

def about(request):
    return render(request, 'bmcem/about.html')

def contact(request):
    return render(request, 'bmcem/contact.html')

def courses(request):
    return render(request, 'bmcem/courses.html')

def blogs (request):
    return render(request, 'bmcem/blog.html')

def admissions(request):
    return render(request, 'admissions.html')

def queries(request):
    return render(request, 'queries.html')

def events(request):
    return render(request, 'events.html')

def notices(request):
    return render(request, 'notices.html')

def careers(request):
    return render(request, 'careers.html')




def admissionquery(request):
    title= "Admission Query"
    if request.method == "POST":
        form = AdmissionQueryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('index'))
            except:
                pass
    else:
        form = AdmissionQueryForm()
    context = {"title": title, "form": form}
    return render(request,'bmcem/form.html',context)


def alumini(request):
    title= "Alumini"
    if request.method == "POST":
        form = AluminiForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('index'))
            except:
                pass
    else:
        form = AluminiForm()
    context = {"title": title, "form": form}
    return render(request,'bmcem/form.html',context)


def query(request):
    title= "Query"
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('index'))
            except:
                pass
    else:
        form = QueryForm()
    context = {"title": title, "form": form}
    return render(request,'bmcem/form.html',context)
