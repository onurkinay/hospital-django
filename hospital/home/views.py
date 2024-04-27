from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import QueryDict 
from patient.forms import PatientForm


import urllib 

from patient.models import Patient
from doctor.models import Doctor
from administrator.models import Administrator
from accountant.models import Accountant

from appointment.models import Appointment
from bill.models import Bill
from department.models import Department


def is_member(user, listgroup):
    return user.groups.filter(name__in=listgroup).exists()

def home(request): 
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    context = {}
    if request.method == "POST":
        if not request.user.is_authenticated:
            user = authenticate(username=request.POST["Email"], password=request.POST["Password"])
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect("/Management")
            else:
                context["message"] = "Invalid username or password"
                return render(request,'login.html',context)
        
    
    if not request.user.is_authenticated:
        return render(request,'login.html')
    else:
        return HttpResponseRedirect("/")
    
def logout(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    else:
        auth_logout(request)
        return HttpResponseRedirect("/")

def register(request):
    context ={}
  
    result = [{}]
    if request.method == "POST": 
        for item in str(request.body)[2:-1].split("&"):
            key, val = item.split("=", 1)
            if key in result[-1]:
                result.append({})
            result[-1][key] = urllib.parse.unquote(val).replace("+"," ")

       

        username = result[0]["Email"]
        name = result[0].pop("Name")
        surname = result[0].pop("Surname")
        password =   result[0].pop("password")
        password_confirm =  result[0].pop("passwordconfirm")

        if password == "" or password_confirm=="":
            context['form']= PatientForm(None)
            context["message"] = "Password is required"
            return render(request, "register.html", context)
        if password != password_confirm:
            context["message"] = "Password is not confirmed"
            context['form']= PatientForm(None)
            return render(request, "register.html", context)
        
        if User.objects.filter(username=username).exists():
            context["message"] = "Email already taken"
            context['form']= PatientForm(None)
            return render(request, "register.html", context)
 

        query_dict = QueryDict('', mutable=True)
        query_dict.update(result[0])

        form = PatientForm(query_dict or None)
        if form.is_valid() and password == password_confirm:
            user = User.objects.create_user(username=username,
                                 email=username,
                                 password=password,first_name=name,last_name=surname) 
            user.save()

            my_group = Group.objects.get(name='Patient')
            my_group.user_set.add(user)

            forme = form.save(commit=False)
            form.instance.User = user 
            forme.save()
            return HttpResponseRedirect("/Login/")
        else:
            context["message"] = form.errors
            return render(request, "register.html", context)
         
    context['form']= PatientForm(None)
    return render(request, "register.html", context)

@login_required
def management(request):
    context ={}
    if is_member(request.user, ["Doctor"]):
        context["data"] = Doctor.objects.get(User_id=request.user.id)
        return render(request, "management/doctor.html", context)
    elif is_member(request.user, ["Patient"]): 
        context["data"] = Patient.objects.get(User_id=request.user.id)
        return render(request, "management/patient.html", context)
    elif is_member(request.user, ["Admin"]): 
        context["data"] = Administrator.objects.get(User_id=request.user.id)

        context["patientCount"] = Patient.objects.all().count()
        context["doctorCount"]= Doctor.objects.all().count()
        context["appCount"]= Appointment.objects.all().count()
        context["billCount"]= Bill.objects.all().count()
        context["deptCount"]= Department.objects.all().count()
        
        return render(request, "management/admin.html", context)
    elif is_member(request.user, ["Accountant"]): 
        context["data"] = Accountant.objects.get(User_id=request.user.id)
        return render(request, "management/accountant.html", context)
   