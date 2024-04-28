from django.contrib import admin
from .models import Tutorial,Course,Events,Category,Student,Teacher,Topic,Outcomes,UserBehaviour,Comment

admin.site.register(UserBehaviour)
admin.site.register(Student)
admin.site.register(Teacher)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Outcomes)
admin.site.register(Comment)

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('event_name',)}
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}