from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name= 'about'),
    path("courses", views.courses, name= 'courses'),
    path("blogs", views.blogs, name= 'blogs'),
    path("careers", views.careers, name= 'careers'),
    path("events", views.events, name= 'events'),
    path("notices", views.notices, name= 'notices'),
    path("admissions", views.admissions, name= 'admissions'),
    path("queries", views.queries, name= 'queries'),
    path("contact", views.contact, name= 'contact')
]