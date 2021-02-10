from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
# from accounts.models import MyUser
# from accounts.models import MyUser


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
        
class Student_profile(models.Model):
    student_id=models.CharField(max_length=50)
    fname = models.CharField(max_length=255, null=True)
    lname = models.CharField(max_length=255, null=True)
    MALE= 1
    FEMALE = 2
    TRANS= 3
    GENDER_CHOICE=(
        (MALE,'Male'),
        (FEMALE,'Female'),
        (TRANS,'TRANS')
    )
    # user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    phone=models.CharField(max_length=20, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    picture = models.ImageField(null=True, upload_to = 'student/static/courses/images/users/', default = 'student/static/courses/images/users/default_user.png')
    linkedin_url =  models.URLField(null=True, max_length=250, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICE, null=True, blank=True)

    class Meta:
        db_table='student'