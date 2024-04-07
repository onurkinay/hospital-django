from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import QueryDict
from patient.models import Patient
from patient.forms import PatientForm
import logging
import urllib


# Create your views here.

def home(request): 
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):  
    if request.method == "POST":
        if not request.user.is_authenticated:
            user = authenticate(username=request.POST["Email"], password=request.POST["Password"])
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseBadRequest("Kullanıcı veya şifre hatalı")
        
    
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
            result[-1][key] = urllib.parse.unquote(val)

       

        username = result[0]["Email"]
        name = result[0].pop("Name")
        surname = result[0].pop("Surname")
        password =   result[0].pop("password")
        password_confirm =  result[0].pop("passwordconfirm")
 

        query_dict = QueryDict('', mutable=True)
        query_dict.update(result[0])

        form = PatientForm(query_dict or None)
        if form.is_valid() and password == password_confirm:
            user = User.objects.create_user(username=username,
                                 email=username,
                                 password=password,first_name=name,last_name=surname)
            user.save()
            forme = form.save(commit=False)
            form.instance.User = user 
            forme.save()
            return HttpResponseRedirect("/Login/")
        else:
            return HttpResponseBadRequest(form.errors)
         
    context['form']= PatientForm(None)
    return render(request, "register.html", context)
