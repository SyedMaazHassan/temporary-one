from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.contrib.auth.models import User
from django import forms
from .models import Student_profile, instructor_profile
from accounts.models import MyUser

# class CreateUserForm(UserCreationForm):
#     #email=forms.EmailField

#     class Meta:
#         model =MyUser
#         fields=['username','email','password1','password2']

class EditStudentProfileForm(UserChangeForm):
    class Meta:
        model = Student_profile
        fields = ('fname', 'lname', 'phone', 'picture','linkedin_url')
        
class EditInstructorProfileForm(UserChangeForm):
    class Meta:
        model = instructor_profile
        fields = ('fname', 'lname', 'phone', 'picture','linkedin_url')
class EditUserForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('email', 'password')