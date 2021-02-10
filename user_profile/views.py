from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from accounts.models import MyUser
from .models import Student_profile, instructor_profile
from course.models import course, order
# from hospital.models import Hospital_profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash,logout
import uuid
from .forms import EditInstructorProfileForm, EditStudentProfileForm, EditUserForm



# Create your views here.

def role_test(user):
    if user.role == "student" or user.role == "Instructor":
        return True
    else:
        return False

# def instructor_role_test(user):
#     if user.role == "Instructor":
#         return True
#     else:
#         return False

def instructors_all_view(request):
    course_data=course.objects.all().select_related('instructor')
    context={'course_data':course_data}
    return render(request,'instructors-all.html',context)
        
@login_required(login_url='/login/')
@user_passes_test(role_test,login_url='/login/')
def user_profile_view(request,id):
    print(role_test)
    if request.user.role == "student":
        profile_data=Student_profile.objects.get(student_id=id)
        profile_edit_form = EditStudentProfileForm(request.POST, request.FILES, instance=profile_data)
        course_data=course.objects.filter(order__user=request.user).select_related('instructor')
        password_change_form=PasswordChangeForm(user=request.user)
        #context={'student_profile_data':student_profile_data,'student_course_data':student_course_data, 'profile_edit_form': profile_edit_form, 'password_change_form':password_change_form}
        context={'profile_data':profile_data,'course_data':course_data, 'profile_edit_form': profile_edit_form, 'password_change_form':password_change_form}
    elif request.user.role == "Instructor":
        profile_data=instructor_profile.objects.get(instructor_id=id)
        profile_edit_form = EditInstructorProfileForm(request.POST, request.FILES, instance=profile_data)
        course_data=course.objects.filter(order__user=request.user) #.select_related('instructor')
        password_change_form=PasswordChangeForm(user=request.user)
    #print('Here is my fname',profile_data.fname )
        context={'profile_data':profile_data, 'profile_edit_form': profile_edit_form, 'password_change_form':password_change_form}
    
    #print(' Is my name ', student_profile_instance.fname)
    if request.method == 'POST': 
        profile_edit_form = EditStudentProfileForm(request.POST, request.FILES, instance=student_profile_data)
        if profile_edit_form.is_valid():
            profile_edit_form.save()
            return render(request,'student_profile.html', context)
            messages.success(request, "Profile was Updated Successfully")
            #return render(request,'student_profile.html',context)
        else:
            print("problem is happening")

    return render(request,'student_profile.html',context)

#@login_required(login_url='/login/')
#@user_passes_test(instructor_role_test,login_url='/login/')
def instructor_details_view(request,id):
    instructor_profile_data=instructor_profile.objects.get(instructor_id=id)
    context = {'instructor_profile_data': instructor_profile_data}
    #student_course_data=course.objects.filter(order__user=request.user)
    #student_course_data = course.object
    #context={'student_profile_data':student_profile_data,'student_course_data':student_course_data} #,'profile_add':profile_add,'title':'Profile'}
    #course_data=Courses.objects.filter(order__user=request.user)
    return render(request,'instructor_profile.html',context)


@login_required(login_url='/login/') 
@user_passes_test(role_test,login_url='/login/')
def editStudent(request,id):
    profile=list(MyUser.objects.filter(id=id).values('email'))
    profile_add=list(Student_profile.objects.filter(id=id).values())
    if request.method == 'POST':
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        country=request.POST.get('country')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        address=request.POST.get('address')
        obj=Student_profile.objects.filter(student_id=id)
        if not obj:
            pt_obj=Student_profile.objects.create(student_id=id,name=name,gender=gender,country=country,age=age,phone=phone,city=city,address=address)
            messages.success(request,'success')
            return redirect(f'/student/{id}/')
        else:
            pt_obj=Student_profile.objects.get(student_id=id)
            pt_obj.name=name
            pt_obj.gender=gender
            pt_obj.country=country
            pt_obj.age=age
            pt_obj.phone=phone
            pt_obj.city=city
            pt_obj.address=address
            pt_obj.save()
            messages.success(request,'success')
            return redirect(f'/student/{id}/')
    return render(request,'student_edit.html',{'profile':profile,'profile_add':profile_add,'title':'Edit Profile'})

@login_required(login_url='/login/')
@user_passes_test(role_test,login_url='/login/')
def passwordChange(request,id):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            logout(request)
            messages.success(request, 'changed')
            return redirect(f'/accounts/login/')
        else:
            logout(request)
            messages.error(request,'error')
            return redirect(f'/accounts/login/')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form,'title':'Change Password'})


def get_list(request,id):
    doc_count=Doctor_profile.objects.filter(is_available=True).count()
    completed=appointments.objects.filter(patient_id=id,is_completed=True,is_rejected=False,is_disabled=False).count()
    upcoming=appointments.objects.filter(patient_id=id,is_confirmed=True,is_rejected=False,is_disabled=False).count()
    waiting=appointments.objects.filter(patient_id=id,is_confirmed=False,is_rejected=False,is_disabled=False).count()
    rejected=appointments.objects.filter(patient_id=id,is_rejected=True,is_disabled=False).count()
    return JsonResponse([doc_count,completed,upcoming,waiting,rejected],safe=False)

#...................................................

# from django.shortcuts import render,redirect
# from django.http import HttpResponse,JsonResponse,Http404
# from django.contrib.auth.decorators import login_required,user_passes_test
# from django.contrib.auth.forms import PasswordResetForm
# from django.contrib import messages
# import uuid
# from .models import Doctor_profile,time_slots,appointments
import datetime,time,os,json
# from accounts.models import MyUser
# # from hospital.models import Hospital_profile,Holidays,Weekends
# from patient.models import Patient_Profile
# from django.template import loader
# from smtplib import SMTPException
# from django.core.mail import send_mail
# from django.core.mail import EmailMessage
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash,logout

mail_send_from="django_appointments@deligence.com"
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
json_dir=os.path.join(BASE_DIR,"data.json")

# Create your views here.


def role_test(user):
    if user.role == "instructor":
        return True
    else:
        return False

def role_test1(user):
    if user.role == "saidatech_admin":
        return True
    else:
        return False

@login_required(login_url='/login/')
@user_passes_test(role_test1,login_url='/login/')
def add_instructor(request):
    #if request.is_ajax():
    print('Helloksdjksdjklsdjlsdjklsd')
    saidatech_admin_id=request.POST.get('saidatech_admin_id')
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    speciality=request.POST.get('speciality')
    country=request.POST.get('country')
    city=request.POST.get('city')
    linkedin_url=request.POST.get('linkedin_url')
    gender=request.POST.get('gender')
    base_link=request.POST.get('link')
    instructor_filter=MyUser.objects.filter(email=email)
    if not instructor_filter:
        id=uuid.uuid4()
        password = MyUser.objects.make_random_password()
        obj=MyUser.objects.create(instructor_id=id,email=email,role='Instructor',is_active=True,is_superuser=False,is_staff=False)
        obj.set_password(password)
        obj.save()
        instructor_object=instructor_profile.objects.create(id=id,fname=name,lanme=lname,email=email,phone=phone,country=country,city=city,speciality=speciality,linkedin_url=linkedin_url,picture=picture,gender=gender)
        doc_object.save()
        link=f"{base_link}/login/"
        html_message=loader.render_to_string('loginmail.html',
            {
                'login':email,
                'password':password,
                'link':link,
                'hospital_name':hospital_name,
                
            })
        subject='Django Appointment System Login Details'
        try:
            mail = send_mail(subject, "Hello",mail_send_from , [email],html_message=html_message)
            message = "success"
        except SMTPException as e:
            print(f'error : {e}')
            message = e
        else:
            message = "Mail could not be sent, Please contact administrator"
        return HttpResponse('Done')
    else:
        return HttpResponse('exists')