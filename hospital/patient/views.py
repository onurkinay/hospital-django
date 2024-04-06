#Patient
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.contrib.auth.models import User
from django.http import QueryDict
from .models import Patient
from .forms import PatientForm
import logging
import urllib

# Create your views here.
def home(request):
    context ={} 
    context["dataset"] = Patient.objects.all()
         
    return render(request, "patient/home.html", context)

def details(request,id): #param id, json return
    queryset = Patient.objects.filter(ID=id).values()
    return JsonResponse(list(queryset),safe=False)
 
def edit(request,id):
    context ={}
    obj = get_object_or_404(Patient, ID = id)
  
    form = PatientForm(request.POST or None, instance = obj) 
  
    result = [{}]
    if request.method == "POST":
        for item in str(request.body)[2:-1].split("&"):
            key, val = item.split("=", 1)
            if key in result[-1]:
                result.append({})
            result[-1][key] = urllib.parse.unquote(val)

       
        UserId = result[0].pop("UserId")
        username = result[0]["Email"]
        name = result[0].pop("Name")
        surname = result[0].pop("Surname")
        password =   result[0].pop("password")
        password_confirm =  result[0].pop("passwordconfirm")
 
        query_dict = QueryDict('', mutable=True)
        query_dict.update(result[0])

        form = PatientForm(query_dict or None, instance = obj) 
        if form.is_valid():
            user = User.objects.get(id=UserId) 
            if password != "" and password_confirm != "":
                if password == password_confirm:
                    user.set_password(password)
                else:
                    return HttpResponseBadRequest("Şifreler farklı")
            user.first_name = name
            user.last_name = surname
            user.username = username
            user.email = username

            user.save()
            form.save()
            return HttpResponseRedirect("/Patients/")
        else:
            return HttpResponseBadRequest(form.errors)
         
    context["form"] = form 
    context["user"] = User.objects.get(id = obj.User_id)
    return render(request, "patient/edit.html", context) 

def delete(request):
    obj = get_object_or_404(Patient, ID = id)
  
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/Doctors/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')



