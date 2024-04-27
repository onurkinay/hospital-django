from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseBadRequest,HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from .models import Department
from .forms import DepartmentForm
from doctor.models import Doctor

def is_member(user, listgroup):
    return user.groups.filter(name__in=listgroup).exists()

@login_required
@user_passes_test(lambda u: is_member(u,["Admin"]))
def home(request):
    context ={} 
    context["dataset"] = Department.objects.all()
         
    return render(request, "department/home.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Accountant"]))
def details(request,id): 
    queryset = Department.objects.filter(ID=id).values()
    return JsonResponse(list(queryset),safe=False)

@login_required
@user_passes_test(lambda u: is_member(u,["Admin"]))
def create(request):
    context ={}
  
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Departments/")
         
    context['form']= form
    return render(request, "department/create.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Admin"]))
def edit(request,id): 
    context ={}
  
    obj = get_object_or_404(Department, ID = id)
  
    form = DepartmentForm(request.POST or None, instance = obj) 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Departments/")
  
    context["form"] = form 
    return render(request, "department/edit.html", context)


@login_required
@user_passes_test(lambda u: is_member(u,["Admin"]))
def delete(request,id):#silinen departmanlara bağlı doktorları ilk departmanlara al
    context ={}
    if id == 1:
        HttpResponseBadRequest('<h1>You can not delete special department</h1>')
    obj = get_object_or_404(Department, ID = id)
  
    if request.method =="POST":

        Doctor.objects.filter(Department_id=id).update(Department_id=1)
        obj.delete() 
        return HttpResponseRedirect("/Departments/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')


@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Patient","Doctor","Accountant"]))
def getDeptName(request,id):
    obj = get_object_or_404(Department, ID = id)
    return HttpResponse(obj.Name)


