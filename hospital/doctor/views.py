from django.http import JsonResponse, HttpResponseBadRequest,HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.contrib.auth.models import User
from django.http import QueryDict
from .models import Doctor
from .forms import DoctorForm
import logging
import urllib
#logger = logging.getLogger('app_api')

def home(request):
    context ={} 
    context["dataset"] = Doctor.objects.all()
         
    return render(request, "doctor/home.html", context)

def details(request,id): 
    queryset = Doctor.objects.filter(ID=id).values()
    return JsonResponse(list(queryset),safe=False)

def create(request):
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
 
        #logger.error(result[0])

        query_dict = QueryDict('', mutable=True)
        query_dict.update(result[0])

        form = DoctorForm(query_dict or None)
        if form.is_valid() and password == password_confirm:
            user = User.objects.create_user(username=username,
                                 email=username,
                                 password=password,first_name=name,last_name=surname)
            user.save()
            forme = form.save(commit=False)
            form.instance.User = user 
            forme.save()
            return HttpResponseRedirect("/Doctors/")
        else:
            return HttpResponseBadRequest(form.errors)
         
    context['form']= DoctorForm(None)
    return render(request, "doctor/create.html", context)


def edit(request,id):  

    context ={}
    obj = get_object_or_404(Doctor, ID = id)
  
    form = DoctorForm(request.POST or None, instance = obj) 
  
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

        form = DoctorForm(query_dict or None, instance = obj) 
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
            return HttpResponseRedirect("/Doctors/")
        else:
            return HttpResponseBadRequest(form.errors)
         
    context["form"] = form 
    context["user"] = User.objects.get(id = obj.User_id)
    return render(request, "doctor/edit.html", context) 

  
   

def delete(request,id):
    obj = get_object_or_404(Doctor, ID = id)
  
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/Doctors/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')

def changeSalary(request, id):#autoration if 
    if request.method =="POST":
        Doctor.objects.filter(ID=id).update(Salary=request.POST["newSalary"])
    return HttpResponse("successfull")


