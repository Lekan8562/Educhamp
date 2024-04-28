from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student,Comment
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('courses','user')

class CustomUserCreationForm(UserCreationForm):
    student = StudentForm()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

