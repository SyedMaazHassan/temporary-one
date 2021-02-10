from django.shortcuts import render
from .models import course

# Create your views here.

def course_details(request, id):
    #course_data=course.objects.get(course_id=id)
    course_data=course.objects.filter(course_code=id).select_related('instructor')[0]
    what_to_learn_list=course_data.course_what_you_will_learn.split(',')

    context={'course_data':course_data, 'what_to_learn_list':what_to_learn_list}
    #course_data=course.objects.filter(order__user=request.user)
    return render(request,'course-details.html', context)

def course_list(request):
    course_data=course.objects.all().select_related('instructor')
    context={'course_data':course_data}
    return render(request,'course-list.html', context)
