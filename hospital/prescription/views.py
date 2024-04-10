from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 
from django.shortcuts import render

from .models import Prescription
from .forms import PrescriptionForm 
from itertools import chain

from doctor.models import Doctor
from patient.models import Patient
from appointment.models import Appointment
from bill.models import Bill

def is_member(user, listgroup):
    return user.groups.filter(name__in=listgroup).exists()
 
@login_required
@user_passes_test(lambda u: is_member(u,["Doctor","Patient"]))
def home(request):
    context ={}  
    if is_member(request.user,["Patient"]):
        patientID = Patient.objects.filter(User_id = request.user.id).values()[0]["ID"]
        appIds = Appointment.objects.filter(PatientID_id = patientID).values("ID").distinct()
        context["dataset"] = Prescription.objects.filter(Appointment_id__in=appIds)
    else:
        doctorId = Doctor.objects.filter(User_id = request.user.id).values()[0]["ID"]
        appIds = Appointment.objects.filter(DoctorID_id = doctorId).values("ID").distinct()
        context["dataset"] = Prescription.objects.filter(Appointment_id__in=appIds)
   
    return render(request, "prescription/home.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Doctor","Patient"]))
def details(request,id): 
    queryset = Prescription.objects.filter(ID=id).values()
    
    return JsonResponse(list(chain(queryset)),safe=False)
  

@login_required
@user_passes_test(lambda u: is_member(u,["Doctor","Patient"]))
def create(request, id):
    context ={}
  
    form = PrescriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Prescriptions/")
         
    context['form']= form
    context["appointment"] = Appointment.objects.filter(ID=id)[0]
    return render(request, "prescription/create.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Doctor"]))
def edit(request,id):
    context ={}
  
    obj = get_object_or_404(Prescription, ID = id)
    form = PrescriptionForm(request.POST or None, instance = obj)
  
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
  
    context["form"] = form
    return render(request, "prescription/edit.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Doctor"]))
def delete(request):
    obj = get_object_or_404(Prescription, ID = id)
    if request.method =="POST": 
        obj.delete() 
        return HttpResponseRedirect("/Prescriptions/")
 
    return HttpResponseBadRequest('<h1>You are not authorized to view this page</h1>')

