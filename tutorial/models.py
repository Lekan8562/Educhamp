from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from froala_editor.fields import FroalaField


class Level(models.TextChoices):
    BEGINNER = "BG","Beginner"
    AMATEUR = "AT","Amateur"
    PROFESSIONAL = "PF","Professional"
    
    


class Category(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    slug = models.SlugField(max_length=100,null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
        
class Topic(models.Model):
    course = models.ForeignKey('Course',on_delete=models.CASCADE,related_name='course_topics',null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    time = models.CharField(max_length=20, null=True, blank=True)
    text = FroalaField()
    order = OrderField(blank=True, for_fields=['course'])
    class Meta:
        verbose_name = 'Topic'
        ordering = ['order']
    def __str__(self):
        return f'{self.order}. {self.name}'
        
class Outcomes(models.Model):
    outcome = models.TextField(null=True,blank=True)
    class Meta:
        verbose_name="Outcome"
    def __str__(self):
        return self.outcome

class Comment(models.Model):
    student = models.ForeignKey('Student',on_delete=models.CASCADE,related_name='student_comments')
    comment = models.TextField()
    course = models.ForeignKey('Course',on_delete=models.CASCADE,related_name='course_comments',null=True)
    topic = models.ForeignKey('Topic',on_delete=models.CASCADE,related_name='topic_comments',null=True)
    def __str__(self):
        return self.comment

class Course(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    slug = models.SlugField(max_length=255,null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    image = models.ImageField(upload_to = "course_images/",null=True)
    old_price = models.DecimalField(max_digits=10,decimal_places=2)
    new_price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ManyToManyField(Category,related_name="courses")
    teacher = models.ForeignKey('Teacher',on_delete=models.CASCADE,null=True)
    outcomes = models.ManyToManyField(Outcomes)
    duration = models.CharField(max_length=100,null=True,blank=True)
    skill_level = models.CharField(max_length=10,choices=Level.choices, default=Level.BEGINNER)
    language = models.CharField(max_length=10,null=True,blank=True)
    assessment = models.BooleanField(default=False)
    description = models.TextField(null=True,blank=True)
    certification=models.TextField(null=True,blank=True)
    #review =
    class Meta:
        verbose_name = "Course"
        ordering = ["-new_price"]
    
    def __str__(self):
        return self.name

class Tutorial(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    slug = models.SlugField(max_length=200,null=False,blank=False)
    courses = models.ManyToManyField(Course,related_name="tutorials")
    founded = models.DateTimeField(auto_now_add=True)
    #teachers =
    #students = 
    image = models.ImageField(upload_to="teachers_image/")
    
    class Meta:
        verbose_name = "Tutorial"
        ordering = ['-founded']
        get_latest_by = 'name'
    
    def __str__(self):
        return self.name

class Events(models.Model):
    event_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    host = models.ForeignKey(Tutorial,on_delete=models.CASCADE,null=True)
    skill_level = models.CharField(max_length=10, choices=Level.choices, default=Level.AMATEUR)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    students_no = models.IntegerField(default=1)
    assessment = models.BooleanField(default=False)
    phone_number = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    date = models.DateField(default=timezone.now)
    time_from = models.TimeField(default=timezone.now)
    time_to = models.TimeField(default=timezone.now)
    image = models.ImageField(upload_to="event_images/",null=True)
    location = models.CharField(max_length=255)
    description = models.TextField(null=True)
    certification = models.TextField(null=True)
    content = models.TextField(null=True)
    
    
    class Meta:
        verbose_name = "Event"
        ordering = ['-date']
        get_latest_by = 'event_name'
    
    def __str__(self):
        return self.event_name
        
        
        
        
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    other_names = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='avatar/images/',null=True        )
    courses = models.ManyToManyField(Course,related_name="students")
    def __str__(self):
        return self.user.username
        

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    others = models.CharField(max_length=150)
    categories = models.ManyToManyField('Category',related_name="category_teachers")
    students = models.ManyToManyField(Student,related_name="teachers")
    avatar = models.ImageField(upload_to='teacher/avatar/',null=True,blank=True)
    def __str__(self):
        return self.user.username

class Content(models.Model):
    topic = models.ForeignKey(Topic, related_name='contents',on_delete=models.CASCADE)    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,limit_choices_to={'model__in':( 'text', 'video', 'image', 'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['topic'])
    class Meta:
        ordering = ['order']


class ItemBase(models.Model):    
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)    
    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True) 
    class Meta:    
        abstract = True 
    def __str__(self): 
        return self.title 
        
class Text(ItemBase):
    content = models.TextField() 
class File(ItemBase):
    file = models.FileField(upload_to='files') 
class Image(ItemBase):       
    file = models.FileField(upload_to='images') 
class Video(ItemBase):
    url = models.URLField()


class UserBehaviour(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    search_count = models.IntegerField(default=0)
    click_count = models.IntegerField(default=0)
    last_interraction = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.user.username} - {self.course.name}'