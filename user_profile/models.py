from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class instructor_profile(models.Model):
    instructor_id=models.UUIDField( primary_key = True, editable = False)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    specialty= models.CharField(max_length=200)
    MALE= 1
    FEMALE = 2
    TRANS= 3
    GENDER_CHOICE=(
        (MALE,'Male'),
        (FEMALE,'Female'),
        (TRANS,'TRANS')
    )
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    picture=models.ImageField(null=True, upload_to = 'accounts/static/accounts/images/users/', default = 'accounts/static/accounts/images/users/default_user.png')
    linkedin_url =  models.URLField(null=True, max_length=250)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICE, null=True, blank=True)


    class Meta:
        db_table='Instructor'



        
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
    picture = models.ImageField(null=True, upload_to = 'accounts/static/accounts/images/users/', default = 'accounts/static/accounts/images/users/default_user.png')
    linkedin_url =  models.URLField(null=True, max_length=250, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICE, null=True, blank=True)

    class Meta:
        db_table='student'
