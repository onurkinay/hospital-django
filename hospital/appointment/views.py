from django.contrib.auth.decorators import login_required, user_passes_test
 

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 

from django.shortcuts import render
from .models import Appointment
from .forms import AppointmentForm


def is_member(user):
    return user.groups.filter(name__in=['Doctor', 'Patient']).exists()

def is_patient(user):
    return user.groups.filter(name__in=['Patient']).exists()

@login_required
@user_passes_test(is_member)
def home(request):
    context ={} 
    context["dataset"] = Appointment.objects.all()
         
    return render(request, "appointment/home.html", context)

@login_required
@user_passes_test(is_member)
def details(request,id): 
    queryset = Appointment.objects.filter(ID=id).values()
    return JsonResponse(list(queryset),safe=False)

@login_required
@user_passes_test(is_patient)
def create(request):
    
    context ={} 
    form = AppointmentForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Appointments/")
         
    context['form']= form
    return render(request, "appointment/create.html", context)
    
@login_required
@user_passes_test(is_member)
def edit(request,id): 
    context ={} 
    obj = get_object_or_404(Appointment, ID= id)
  
    form = AppointmentForm(request.POST or None, instance = obj)
     
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Appointments/")
    
    
    context["form"] = form
 
    return render(request, "appointment/edit.html", context)

@login_required
@user_passes_test(is_member)
def delete(request,id):
    obj = get_object_or_404(Appointment, ID = id)
  
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/Appointments/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')


