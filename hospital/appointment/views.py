from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 

from django.shortcuts import render
from .models import Appointment
from .forms import AppointmentForm


def home(request):
    context ={} 
    context["dataset"] = Appointment.objects.all()
         
    return render(request, "appointment/home.html", context)

def details(request,id): #param id
    queryset = Appointment.objects.filter(ID=id).values()
    return JsonResponse(list(queryset),safe=False)

def create(request):
   
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = AppointmentForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Appointments/")
         
    context['form']= form
    return render(request, "appointment/create.html", context)
    

def edit(request,id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Appointment, ID= id)
 
    # pass the object as instance in form
    form = AppointmentForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Appointments/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "appointment/edit.html", context)

def delete(request,id):
    obj = get_object_or_404(Appointment, ID = id)
  
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/Appointments/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')
