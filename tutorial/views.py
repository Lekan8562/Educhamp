from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import StudentForm,CustomUserCreationForm,CommentForm



def home(request):
    
    courses = Course.objects.all()
    events = Events.objects.all()
    context={'courses':courses,'events':events}
    if request.user.is_authenticated:
        return redirect('logout')
    return render(request,'tutorial/home.html',context)
    
    
    
#TEACHER
def teacher_profile(request):
    context = {}
    return render(request,'regiatration/teachers_profile.html',context)
    
    
    
    

   
def student_home(request):
    courses = Course.objects.all()
    events = Events.objects.all()
    if request.user.is_authenticated:
        student = request.user.student
        context = {'courses':courses,'events':events,'student':student}
        return render(request,'tutorial/student_home.html',context)
    else:
        context = {'courses':courses,'events':events}
        return render(request,'tutorial/student_home.html',context)
        
def student_courses(request,pk):
    student = get_object_or_404(Student,pk=pk)
    context = {'student':student,'courses':courses}
    return render(request,"tutorial/student_courses.html",context)

def student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {'student':student}
    return render(request,"tutorial/student_profile.html",context)
    
def dashboard(request):
    context = {}
    return render(request,"tutorial/activity.html",context)

def mail(request):
    context = {}
    return render(request,"tutorial/mail.html",context)
    
    
def courses(request):
    courses = Course.objects.all()
    context={'courses':courses}
    return render(request,'tutorial/courses.html',context)

def course_detail(request,course_id):
    course = get_object_or_404(Course,id=course_id)
    comments = course.course_comments.all()
    teacher = Teacher.objects.all()
    context = {"course":course,'teacher':teacher,'comments':comments}
    return render(request,"tutorial/course_detail.html",context)

def topic_detail(request, topic_slug):
    topic = get_object_or_404(Topic, slug__iexact=topic_slug)
    comments = topic.topic_comments.all()
    student = request.user.student
    if request.method == "POST":
        comment = request.POST.get('comment')
        Comment.objects.create(student=student,topic=topic,comment=comment)
        return redirect(request.META.get('HTTP_REFERER'))
    context = {'topic':topic,'student':student,'comments':comments}
    return render(request, 'tutorial/topic_detail.html',context)


        

def event_detail(request,slug):
    teacher = Teacher.objects.all()
    event = get_object_or_404(Events,slug__iexact=slug)
    context = {"event": event,'teacher':teacher}
    return render(request,"tutorial/event_detail.html",context)


def registerPage( request):
    form = CustomUserCreationForm
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            login(request,user)
            return redirect('student_home')
        else:
            messages.error(request,"An error occurred during registration")
    context={'form':form}
    return render(request,"registration/register.html",context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username or Password does not exist')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('student_home')
    context = {}
    return render(request,"registration/login.html",context)

def logoutUser(request):
    logout(request)
    return redirect('home')