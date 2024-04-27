from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.contrib.auth.models import User,Group
from django.http import QueryDict
from .models import Patient, BLOOD_GROUPS
from .forms import PatientForm 
import urllib

from itertools import chain


def is_member(user, listgroup):
    return user.groups.filter(name__in=listgroup).exists()
 
@login_required
@user_passes_test(lambda u: is_member(u,["Admin"]))
def home(request):
    context ={} 
    context["dataset"] = Patient.objects.all()
         
    return render(request, "patient/home.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Patient","Admin","Doctor"]))
def details(request,id):  
    queryset = Patient.objects.filter(ID=id).values()
    
    patientUser = User.objects.filter(id=queryset[0]["User_id"]).values("first_name","last_name","email")
    jsonResult = list(chain(queryset,patientUser))
    jsonResult[0]["Blood_Group"] = BLOOD_GROUPS[ int( jsonResult[0]["Blood_Group"] )-1 ][1]
    return JsonResponse(jsonResult,safe=False)
    
 
@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Patient"]))
def edit(request,id=-1):
    if id == -1:
        id =Patient.objects.filter(User_id = request.user.id).values()[0]["ID"]
    context ={}
    obj = get_object_or_404(Patient, ID = id)
  
    form = PatientForm(request.POST or None, instance = obj) 
  
    result = [{}]
    if request.method == "POST":
       
        for item in str(request.body).split("&"):
            key, val = item.split("=", 1)
            if key in result[-1]:
                result.append({})
            result[-1][key] = urllib.parse.unquote(val).replace("+"," ").replace("'","")

       
        UserId = result[0].pop("UserId")
        username = result[0]["Email"]
        name = result[0].pop("Name")
        surname = result[0].pop("Surname")
        password =   result[0].pop("password")
        password_confirm =  result[0].pop("passwordconfirm")

        
        IsChangePassword = False
        if password != "" or password_confirm!="": 
            if password != password_confirm:
                context["message"] = "Password is not confirmed"
                context["form"] = form 
                context["user"] = User.objects.get(id = obj.User_id)
                return render(request, "patient/edit.html", context)
            IsChangePassword = True
        
        if username != User.objects.filter(id = obj.User_id).values()[0]["username"]:
            if User.objects.filter(username=username).exists():
                context["message"] = "Email already taken"
                context["form"] = form 
                context["user"] = User.objects.get(id = obj.User_id)
                return render(request, "patient/edit.html", context)
 
 
        query_dict = QueryDict('', mutable=True)
        query_dict.update(result[0])

        form = PatientForm(query_dict or None, instance = obj) 
        if form.is_valid():
            user = User.objects.get(id=UserId) 
            if IsChangePassword:
                user.set_password(password)
            user.first_name = name
            user.last_name = surname
            user.username = username
            user.email = username

            user.save()
            form.save()
            if is_member(request.user,["Admin"]):
                return HttpResponseRedirect("/Patients/")
            else:
                return HttpResponseRedirect("/Management/")
        else:
            context["message"] = form.errors
            context["form"] = form 
            context["user"] = User.objects.get(id = obj.User_id)
            return render(request, "patient/edit.html", context)
         
    context["form"] = form 
    context["user"] = User.objects.get(id = obj.User_id)
    return render(request, "patient/edit.html", context) 

@login_required
@user_passes_test(lambda u: is_member(u,["Admin"]))
def delete(request):
    if request.method =="POST":
        Patient.objects.filter(ID=id).update(IsVisible=False)
        return HttpResponseRedirect("/Patients/") 
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')



