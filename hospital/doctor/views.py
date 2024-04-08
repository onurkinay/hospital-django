from django.contrib.auth.decorators import login_required, user_passes_test

from django.http import JsonResponse, HttpResponseBadRequest,HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.contrib.auth.models import User,Group
from django.http import QueryDict
from .models import Doctor
from .forms import DoctorForm
import urllib
from itertools import chain


def is_member(user, listgroup):
    return user.groups.filter(name__in=listgroup).exists()
 

@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Accountant"]))
def home(request):
    context ={} 
    context["dataset"] = Doctor.objects.all()
         
    return render(request, "doctor/home.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Doctor","Patient"])) #sadece giriş yapan doktor kend bilgileri erişebilir
def details(request,id): 
    queryset = Doctor.objects.filter(ID=id).values()
    doctorUser = User.objects.filter(id=queryset[0]["User_id"]).values("first_name","last_name","email")
    return JsonResponse(list(chain(queryset,doctorUser)),safe=False)

@login_required
@user_passes_test(lambda u: is_member(u,["Admin"]))
def create(request):
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
 
        #logger.error(result[0])

        query_dict = QueryDict('', mutable=True)
        query_dict.update(result[0])

        form = DoctorForm(query_dict or None)
        if form.is_valid() and password == password_confirm:
            user = User.objects.create_user(username=username,
                                 email=username,
                                 password=password,first_name=name,last_name=surname)
            user.save()

            my_group = Group.objects.get(name='Doctor')
            my_group.user_set.add(user)

            forme = form.save(commit=False)
            form.instance.User = user 
            forme.save()
            return HttpResponseRedirect("/Doctors/")
        else:
            return HttpResponseBadRequest(form.errors)
         
    context['form']= DoctorForm(None)
    return render(request, "doctor/create.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Doctor"]))
def edit(request,id=-1):  
    if id == -1:
          id = Doctor.objects.filter(User_id = request.user.id).values()[0]["ID"]
    context ={}
    obj = get_object_or_404(Doctor, ID = id)
  
    form = DoctorForm(request.POST or None, instance = obj) 
  
    result = [{}]
    if request.method == "POST":
        for item in str(request.body.decode('utf-8'))[2:-1].split("&"):
            key, val = item.split("=", 1)
            if key in result[-1]:
                result.append({})
            result[-1][key] = urllib.parse.unquote(val).replace("+"," ")

       
        UserId = result[0].pop("UserId")
        username = result[0]["Email"]
        name = result[0].pop("Name")
        surname = result[0].pop("Surname")
        password =   result[0].pop("password")
        password_confirm =  result[0].pop("passwordconfirm")

        if password == "" or password_confirm=="":
            context["form"] = form 
            context["user"] = User.objects.get(id = obj.User_id)
            context["message"] = "Password is required"
            return render(request, "doctor/edit.html", context)
        if password != password_confirm:
            context["message"] = "Password is not confirmed"
            context["form"] = form 
            context["user"] = User.objects.get(id = obj.User_id)
            return render(request, "doctor/edit.html", context)
        
        if User.objects.filter(username=username).exists():
            context["message"] = "Email already taken"
            context["form"] = form 
            context["user"] = User.objects.get(id = obj.User_id)
            return render(request, "doctor/edit.html", context)
 
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
            if is_member(request.user,["Admin"]):
                return HttpResponseRedirect("/Doctors/")
            else:
                return HttpResponseRedirect("/Management/")
        else:
            context["message"] = form.errors
            context["form"] = form 
            context["user"] = User.objects.get(id = obj.User_id)
            return render(request, "doctor/edit.html", context)
         
    context["form"] = form 
    context["user"] = User.objects.get(id = obj.User_id)
    return render(request, "doctor/edit.html", context) 

  

@login_required
@user_passes_test(lambda u: is_member(u,["Admin"]))
def delete(request,id):
    obj = get_object_or_404(Doctor, ID = id)
  
    if request.method =="POST": 
        obj.delete() 
        return HttpResponseRedirect("/Doctors/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')

@login_required
@user_passes_test(lambda u: is_member(u,["Accountant"]))
def changeSalary(request, id): 
    if request.method =="POST":
        Doctor.objects.filter(ID=id).update(Salary=request.POST["newSalary"])
    return HttpResponse("successfull")


