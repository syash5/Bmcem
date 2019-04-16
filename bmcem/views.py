from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404 

# Create your views here.

    
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
    



