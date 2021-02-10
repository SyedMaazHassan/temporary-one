from django.contrib import admin
from .models import course, order 

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display=('course_code','name','price', 'duration', 'instructor', 'lecture_days', 'start_time', 'end_time', 'course_img')
     
admin.site.register(course, CourseAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=('date_created','user','course')

admin.site.register(order, OrderAdmin)
