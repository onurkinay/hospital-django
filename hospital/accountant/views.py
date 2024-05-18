from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseBadRequest,HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.contrib.auth.models import User,Group
from django.http import QueryDict

from accountant.models import Accountant
from .forms import AccForm
import urllib
from itertools import chain



def is_member(user, listgroup): #check roles for users
    return user.groups.filter(name__in=listgroup).exists()


@login_required # not allowed anon
@user_passes_test(lambda u: is_member(u,["Admin",])) #just admin can access
def home(request):
    context ={} 
    context["dataset"] = Accountant.objects.filter(IsVisible=True) #get accountant which is visible
    return render(request, "accountant/home.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Admin",])) #just admin can access
def details(request,id): 
    queryset = Accountant.objects.filter(ID=id).values()
    adminUser = User.objects.filter(id=queryset[0]["User_id"]).values("first_name","last_name","email")
    return JsonResponse(list(chain(queryset,adminUser)),safe=False)#merge two info accountant and user
 
@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Accountant"]))
def edit(request,id=-1):  
    if id == -1:#logged in user info
          id = Accountant.objects.filter(User_id = request.user.id).values()[0]["ID"]
    context ={}
    obj = get_object_or_404(Accountant, ID = id)#get accountant row or throw 404
  
    form = AccForm(request.POST or None, instance = obj) 
  
    result = [{}]
    if request.method == "POST":
        for item in str(request.body.decode('utf-8')).split("&"): #divide into user and accountant table info
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
        
        IsChangePassword = False  
        if password != "" or password_confirm!="": #check password is not empty
            if password != password_confirm:
                context["message"] = "Password is not confirmed"
                context["form"] = form 
                context["user"] = User.objects.get(id = obj.User_id)
                return render(request, "accountant/edit.html", context)
            IsChangePassword = True
            
        if username != User.objects.filter(id = obj.User_id).values()[0]["username"]:
            if User.objects.filter(username=username).exists():
                context["message"] = "Email already taken"
                context["form"] = form 
                context["user"] = User.objects.get(id = obj.User_id)
                return render(request, "accountant/edit.html", context)
 
        query_dict = QueryDict('', mutable=True)
        query_dict.update(result[0])

        form = AccForm(query_dict or None, instance = obj) 
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
           
            return HttpResponseRedirect("/Accountants/")
            
        else:
            context["message"] = form.errors
            context["form"] = form 
            context["user"] = User.objects.get(id = obj.User_id)
            return render(request, "accountant/edit.html", context)
         
    context["form"] = form 
    context["user"] = User.objects.get(id = obj.User_id)
    return render(request, "accountant/edit.html", context) 

  

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

        query_dict = QueryDict('', mutable=True)
        query_dict.update(result[0])

        form = AccForm(query_dict or None)

        if User.objects.filter(username=username).exists():
            context["message"] = "Email already taken"
            context["form"] = form  
            return render(request, "administrator/edit.html", context)

        
        if form.is_valid() and password == password_confirm:
            user = User.objects.create_user(username=username,
                                 email=username,
                                 password=password,first_name=name,last_name=surname)
            user.save()

            my_group = Group.objects.get(name='Accountant')
            my_group.user_set.add(user)

            forme = form.save(commit=False)
            form.instance.User = user 
            forme.save()
            return HttpResponseRedirect("/Accountants/")
        else:
            return HttpResponseBadRequest(form.errors)
         
    context['form']= AccForm(None)
    return render(request, "accountant/create.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Admin"]))
def delete(request,id):
    if request.method =="POST" and id!=1:
        Accountant.objects.filter(ID=id).update(IsVisible=False)
        return HttpResponseRedirect("/Accountants/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')

