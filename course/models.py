from django.db import models
from user_profile.models import instructor_profile
from accounts.models import MyUser
class course(models.Model):
    course_code =  models.CharField(primary_key = True, max_length=6)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    duration=models.CharField(max_length=255)
    instructor=models.ForeignKey(instructor_profile, on_delete=models.CASCADE)
    lecture_days=models.CharField(max_length=255)
    start_time = models.TimeField((u"Conversation Time"), blank=True)
    end_time = models.TimeField((u"Conversation Time"), blank=True)
    course_img=models.ImageField(null=True, upload_to = 'courses/static/courses/images/courses/', default = 'courses/static/courses/images/courses/default_course.jpg')
    course_description=models.TextField(null=True)
    course_what_you_will_learn=models.TextField(null=True)
    Requirements=models.TextField(null=True)

class order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null = True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    ACCEPTED= 1
    DECLINED = 2
    PENDING= 3
    ORDER_STATUS_CHOICE=(
        (ACCEPTED,'Accepted'),
        (DECLINED,'Declined'),
        (PENDING,'Pending')
    )
    order_status = models.PositiveSmallIntegerField(choices=ORDER_STATUS_CHOICE, null=True, blank=True)
