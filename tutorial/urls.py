from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('',views.home,name="home"),
        path('home/',views.student_home,name='student_home'),
        path("student/<int:pk>/",views.student_courses,name="student_courses"),
        path('student/<int:student_id>/profile/',views.student_profile,name="student_profile"),
        path("dashboard/",views.dashboard,name="dashboard"),
        path('messages/',views.mail,name="mail"),
        
        path("courses/",views.courses,name="courses"),
        path('<int:course_id>/course/',views.course_detail,name="course_detail"),
        path('topic/<slug:topic_slug>/',views.topic_detail,name='topic_detail'),
        path('<slug:slug>/events/',views.event_detail,name="event_detail"),
        
        
        path('register/',views.registerPage,name="register"),
        
        
        path('login/',views.loginPage,name="login"),
        path('logout/',views.logoutUser,name="logout"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)