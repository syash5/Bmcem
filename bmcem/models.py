from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import datetime
# Create your models here.



#Users

class UserProfile(AbstractUser):

    username = models.CharField('username', max_length=100, unique=True, default="username Should be more than 6 letters,alphanumeric and first letter should be alphabet")
    full_name= models.CharField(max_length=50, default="",blank= False)
    dob = models.DateField(auto_now_add=True, blank=False)

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    password= models.CharField(max_length=150,blank=False, default="")
    email = models.EmailField(unique=True, blank=False)
    contact_no = models.CharField(max_length=100,unique=False, blank=False)
    Address = models.CharField(max_length=100, null=True )

    USERNAME_FIELD = 'email'  # use email to log in
    REQUIRED_FIELDS = ['username']  # required when user is created

    def __str__(self):
        return str(self.username)
    class Meta:
        db_table = "users"


#Gallery

class Gallery(models.Model):
    title = models.CharField(max_length=100,default="")
    photos = models.ImageField(default='default.png', blank=True)



#Blogs

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(default='Body')
    date = models.DateTimeField(auto_now_add=True, blank=False)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # school = models.OneToOneField(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:150] + '...'


#notifications


class Notification(models.Model):
    desciption = models.TextField()
    created_at = models.TimeField()
    file = models.FileField()


#Newsletter

class NewsLetter(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE) #or email


#Student Admission Query Models

class AdmissionQuery(models.Model):
    full_name = models.CharField(max_length=50, default="", blank=False)
    dob = models.DateField(auto_now_add=True, blank=False)
    last_edu_qualification = models.CharField(max_length=150,default="Please Mention Your Last Educational Qualification")
    applying_for = models.CharField(max_length=150,default="Which Programme You Want To Apply For")
    branch = models.CharField(max_length=100,default="Mention The Branch You Want To Apply For")
    place = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100,blank=False)
    email = models.EmailField(default="abc@gmail.com",blank=False)
    detail = models.TextField()



#Alumini Models

class Alumini(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    current_org = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    enterpreneur = models.CharField(max_length=100, default= "If yes, Please Mention the details about your organisation.")
    other_detail = models.CharField(max_length=100)



# contact us form

class Query(models.Model):
    full_name = models.CharField(max_length=50, default="", blank=False)
    contact_no = models.CharField(max_length=100,blank=False)
    email = models.EmailField(default="abc@gmail.com",blank=False)
    detail = models.TextField()


    def __str__(self):
        return self.full_name