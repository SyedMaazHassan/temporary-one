from django.contrib import admin
from .models import Student_profile, instructor_profile

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display=('student_id','fname', 'lname', 'city', 'phone', 'country', 'picture', 'linkedin_url', 'gender')
     
admin.site.register(Student_profile, StudentAdmin)


class InstructorAdmin(admin.ModelAdmin):
    list_display=('instructor_id','fname', 'lname','phone','specialty','country','city','picture','linkedin_url', 'gender')
     
admin.site.register(instructor_profile, InstructorAdmin)
