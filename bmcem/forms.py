from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm






class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = [
                  "username",
                  "full_name",
                  "email",
                  "contact_no",
                  "Address",
                  "password1",
                  "password2"
                  ]


    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 5:
            raise forms.ValidationError("Username must be more than 5 characters.")
        return username


    def clean_contact(self):
        contact_no = self.cleaned_data('contact_no')
        if len(contact_no)<10:
            return forms.ValidationError("Invalid Contact,Please Enter 10digit Contact Number")


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['full_name']
        if commit:
            user.save()
        return user


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields =  '__all__'


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields =  '__all__'


class AdmissionQueryForm(forms.ModelForm):
    class Meta:
        model = AdmissionQuery
        fields =  '__all__'


class AluminiForm(forms.ModelForm):
    class Meta:
        model = Alumini
        fields =  '__all__'



class QueryForm(forms.Form):
    class Meta:
        model = Query
        fields =  '__all__'



