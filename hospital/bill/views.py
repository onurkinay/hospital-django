from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseBadRequest,HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 

from django.shortcuts import render

from .models import Bill
from .forms import BillForm

from appointment.models import Appointment
from patient.models import Patient


def is_member(user, listgroup):
    return user.groups.filter(name__in=listgroup).exists()

@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Patient","Accountant"]))
def home(request):
    context ={} 
    if is_member(request.user,["Patient"]):
        patientID = Patient.objects.filter(User_id = request.user.id).values()[0]["ID"]
        appIds = Appointment.objects.filter(PatientID_id = patientID).values("ID").distinct()
        context["dataset"] = Bill.objects.filter(Appointment_id__in=appIds) 
    
    else:
        context["dataset"] = Bill.objects.all() 
    
    return render(request, "bill/home.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Admin","Patient","Accountant"]))
def details(request): #param id
    queryset = Bill.objects.filter(ID=id).values()
    return JsonResponse({"Bill": list(queryset)})

@login_required
@user_passes_test(lambda u: is_member(u,["Accountant"]))
def create(request): 
    context ={}
  
    form = BillForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "bill/create.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Accountant"]))
def edit(request,id): 
    context ={}
  
    obj = get_object_or_404(Bill, ID = id)
  
    form = BillForm(request.POST or None, instance = obj)
  
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Bills/")
  
    context["form"] = form
 
    return render(request, "bill/edit.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Accountant"]))
def delete(request):
    obj = get_object_or_404(Bill, ID = id)
  
    if request.method =="POST": 
        obj.delete() 
        return HttpResponseRedirect("/Bills/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')

@login_required
@user_passes_test(lambda u: is_member(u,["Patient"]))
def payment(request, id):
    if request.method =="POST":
        Bill.objects.filter(ID=id).update(IsPaid=1)
    return HttpResponse("success")