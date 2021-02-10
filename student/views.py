from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from accounts.models import MyUser
from .models import Student_profile
# from hospital.models import Hospital_profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash,logout
import uuid


# Create your views here.
def role_test(user):
    if user.role == "student":
        return True
    else:
        return False
        
@login_required(login_url='/login/')
@user_passes_test(role_test,login_url='/login/')
def student_view(request,id):
    #obj=Student_profile.objects.filter(student_id=id)
    student_profile_data=Student_profile.objects.get(student_id=id)
    context={'student_profile_data':student_profile_data} #,'profile_add':profile_add,'title':'Profile'}
    #course_data=Courses.objects.filter(order__user=request.user)
    return render(request,'student_profile.html',context)



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

@login_required(login_url='/login/')
def getwatingappointments(request,id):
    check=request.GET.get('type')
    if check == 'waiting':
        obj=list(appointments.objects.filter(patient_id=id,is_confirmed=False,is_rejected=False,is_disabled=False).values())
    elif check == 'upcoming':
        obj=list(appointments.objects.filter(patient_id=id,is_confirmed=True,is_rejected=False,is_disabled=False).values())
    elif check == 'completed':
        obj=list(appointments.objects.filter(patient_id=id,is_completed=True,is_rejected=False,is_disabled=False).values())
    elif check == 'rejected':
        obj=list(appointments.objects.filter(patient_id=id,is_rejected=True,is_disabled=False).values())
    else:
        return JsonResponse([],safe=False)
    if obj:
        
        for item in obj:
            doc_obj=list(Doctor_profile.objects.filter(id=item.get('doctor_id')).values())[0]
            hos_obj=list(Hospital_profile.objects.filter(id=doc_obj.get('hospital_id')).values())[0]
            item['doctor_name']=doc_obj.get('name')
            item['doctor_qualification']=doc_obj.get('qualification')
            item['doctor_speciality']=doc_obj.get('speciality')
            item['hospital_name']=hos_obj.get('name')
    return JsonResponse(obj,safe=False)

def get_list(request,id):
    doc_count=Doctor_profile.objects.filter(is_available=True).count()
    completed=appointments.objects.filter(patient_id=id,is_completed=True,is_rejected=False,is_disabled=False).count()
    upcoming=appointments.objects.filter(patient_id=id,is_confirmed=True,is_rejected=False,is_disabled=False).count()
    waiting=appointments.objects.filter(patient_id=id,is_confirmed=False,is_rejected=False,is_disabled=False).count()
    rejected=appointments.objects.filter(patient_id=id,is_rejected=True,is_disabled=False).count()
    return JsonResponse([doc_count,completed,upcoming,waiting,rejected],safe=False)



