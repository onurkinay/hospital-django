#Prescription
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.shortcuts import render

from .models import Prescription
from .forms import PrescriptionForm 
def home(request):
    context ={}
  
    context["dataset"] = Prescription.objects.all() 
    return render(request, "prescription/home.html", context)

def details(request,id): 
    queryset = Prescription.objects.filter(ID=id).values()
    return JsonResponse(list(queryset),safe=False)

def create(request, id):
    context ={}
  
    form = PrescriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "prescription/create.html", context)

def edit(request,id):
    context ={}
  
    obj = get_object_or_404(Prescription, ID = id)
    form = PrescriptionForm(request.POST or None, instance = obj)
  
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
  
    context["form"] = form
    return render(request, "prescription/edit.html", context)

def delete(request):
    obj = get_object_or_404(Prescription, ID = id)
    if request.method =="POST": 
        obj.delete() 
        return HttpResponseRedirect("/Prescriptions/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')

