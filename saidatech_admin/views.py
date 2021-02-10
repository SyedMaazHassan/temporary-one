from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse,JsonResponse
from .models import saidatech_admin_profile
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash,logout
from user_profile.models import Student_profile, instructor_profile
from accounts.models import MyUser
from django.template import loader
from smtplib import SMTPException
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import datetime,time
import uuid
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text
from django.urls import reverse_lazy, reverse
from accounts.utils import generate_token
#from user_profile.views import add_instructor

# Create your views here.

mail_send_from="django_appointments@deligence.com"

def role_test(user):
    #if user.role == "saidatech_admin":
    if user.is_admin:
        return True
    else:
        return False

# @login_required(login_url='/login/')
# @user_passes_test(role_test1,login_url='/login/')
def add_instructor(request):
    print('Helloksdjksdjklsdjlsdjklsd',request.method)
    saidatech_admin_id=request.POST.get('saidatech_admin_id')
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    specialty=request.POST.get('specialty')
    country=request.POST.get('country')
    city=request.POST.get('city')
    linkedin_url=request.POST.get('linkedin_url')
    gender=request.POST.get('gender')
    instructor_login_link=request.POST.get('link')
    instructor_filter=MyUser.objects.filter(email=email)
    domain = get_current_site(request).domain
    #link=reverse('password_reset_confirm', kwargs={'uidb64':uidb64,'token':generate_token.make_token(user)})
    #link='/password_reset_confirm'
    if not instructor_filter:
        id=uuid.uuid4()
        password = MyUser.objects.make_random_password()
        obj=MyUser.objects.create(id=id,email=email,role='Instructor',is_active=True)
        obj.set_password(password)
        obj.save()
        instructor_object=instructor_profile.objects.create(instructor_id=id,phone=phone,fname=fname,lname=lname,country=country,city=city,linkedin_url=linkedin_url,picture="",gender=gender)
        instructor_object.save()

        uidb64=urlsafe_base64_encode(force_bytes(obj.pk)).decode()
        domain = get_current_site(request).domain
        #link=reverse('password_reset_confirm:reset', kwargs={'uidb64':uidb64,'token':generate_token.make_token(obj)})
        link='/reset_password'
        pass_reset_link='http://'+ domain + link 
        #'http://'+ domain + link + '/'+ uidb64 + '/'+ generate_token.make_token(obj)
        print('Here is the pass_reset_link ', pass_reset_link)

        #pass_reset_link='http://'+ domain + link
        
        html_message=loader.render_to_string('loginmail.html',
            {
                'login':email,
                'password':password,
                'link':pass_reset_link,
                #'hospital_name':hospital_name,
                
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
        print("user already exist")
        return HttpResponse('exists')

@login_required(login_url='/login/')
@user_passes_test(role_test,login_url='/login/')
def saidatech_admin_view(request,id):
    if request.method=='POST':        
        add_instructor(request)
         #add a confirmatn
    
    profile=saidatech_admin_profile.objects.filter(saidatech_admin_id=id)
    if not profile:
        return redirect(f'/editHospital/{id}/')
    else:
        profile=list(saidatech_admin_profile.objects.filter(saidatech_admin_id=id).values('fname','lname','email','phone'))
        return render(request,'saidatech_admin_profile.html',{'profile':profile,'title':"Profile"})


@login_required(login_url='/login/')
@user_passes_test(role_test,login_url='/login/')
def saidatech_admin_edit(request,id):
    profile=list(saidatech_admin_profile.objects.filter(id=id).values('name','email','country','city','beds_count','phone'))
    if request.method == 'POST':
        print('Helloksdjksdjklsdjlsdjklsd')
        #add_instructor(request)
        #confirm you added instructor
    hospital_name=request.POST.get('hospital_name')
    email=request.POST.get('hos_email')
    beds_count=request.POST.get('no_of_beds')
    phone=request.POST.get('hos_phone')
    city=request.POST.get('hos_city')
    country=request.POST.get('country')
    filter_obj=saidatech_admin_profile.objects.filter(id=id)
    if not filter_obj:
        obj=saidatech_admin_profile.objects.create(id=id,name=hospital_name,email=email,country=country,city=city,beds_count=beds_count,phone=phone)
        obj.save()
        messages.success(request,'success')
        return redirect(f'/hospital/{id}/')
    else:
        edit_obj=saidatech_admin_profile.objects.get(id=id)
        edit_obj.name=hospital_name
        edit_obj.email=email
        edit_obj.country=country
        edit_obj.city=city
        edit_obj.beds_count=beds_count
        edit_obj.phone=phone
        edit_obj.save()
        messages.success(request,'success')
        return redirect(f'/hospital/{id}/')
    return render(request,'hospital_edit.html',{'profile':profile,'title':'Edit Profile'})


@login_required(login_url='/login/')
@user_passes_test(role_test,login_url='/login/')
def changePassword(request,id):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            logout(request)
            messages.success(request, 'changed')
            return redirect(f'/login/')
        else:
            logout(request)
            messages.error(request,'error')
            return redirect(f'/login/')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form,'title':'Change Password'})
