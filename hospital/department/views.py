from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from .models import Department
from .forms import DepartmentForm
# Create your views here.
def home(request):
    context ={} 
    context["dataset"] = Department.objects.all()
         
    return render(request, "department/home.html", context)

def details(request,id): 
    queryset = Department.objects.filter(ID=id).values()
    return JsonResponse({"department": list(queryset)})

def create(request):
    context ={}
  
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Departments/")
         
    context['form']= form
    return render(request, "department/create.html", context)


def edit(request,id): 
    context ={}
  
    obj = get_object_or_404(Department, ID = id)
  
    form = DepartmentForm(request.POST or None, instance = obj) 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Departments/")
  
    context["form"] = form 
    return render(request, "department/edit.html", context)

def delete(request,id):
    context ={}
    if id == 1:
        HttpResponseBadRequest('<h1>You are not delete special department</h1>')
    # fetch the object related to passed id
    obj = get_object_or_404(Department, ID = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/Departments/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')


