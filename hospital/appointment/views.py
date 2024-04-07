from django.contrib.auth.decorators import login_required, user_passes_test
 

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.shortcuts import render

from .models import Appointment
from doctor.models import Doctor
from patient.models import Patient
from bill.models import Bill

from .forms import AppointmentForm
from itertools import chain
from datetime import datetime

def is_member(user, listgroup):
    return user.groups.filter(name__in=listgroup).exists()

@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Patient","Doctor"]))
def home(request):
    context ={} 
    context["dataset"] = Appointment.objects.all() 
    return render(request, "appointment/home.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Patient","Doctor"]))
def details(request,id): 
    queryset = Appointment.objects.filter(ID=id).values()  

    return JsonResponse(list(chain(queryset)),safe=False)

@login_required
@user_passes_test(lambda u: is_member(u,["Patient"]))
def create(request):
    
    context ={} 
    form = AppointmentForm(request.POST or None)
    
    if form.is_valid():
       
        form.save()

        b = Bill(IssuedDate=datetime.now(), Amount=100, IsPaid=False,Appointment=form.instance)
        b.save() 
        return HttpResponseRedirect("/Appointments/") 
    context['form']= form
    return render(request, "appointment/create.html", context)
    
@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Patient","Doctor"]))
def edit(request,id): 
    context ={} 
    obj = get_object_or_404(Appointment, ID= id)
  
    form = AppointmentForm(request.POST or None, instance = obj)
     
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Appointments/")
    
    
    context["form"] = form
 
    return render(request, "appointment/edit.html", context)

@user_passes_test(lambda u: is_member(u,["Admin","Patient","Doctor"]))
def delete(request,id):
    obj = get_object_or_404(Appointment, ID = id)
  
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/Appointments/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')


