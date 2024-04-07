from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.shortcuts import render

from .models import Prescription
from .forms import PrescriptionForm 

def is_member(user, listgroup):
    return user.groups.filter(name__in=listgroup).exists()
 
@login_required
@user_passes_test(lambda u: is_member(u,["Doctor","Patient"]))
def home(request):
    context ={}
  
    context["dataset"] = Prescription.objects.all() 
    return render(request, "prescription/home.html", context)

@login_required
@user_passes_test(lambda u: is_member(u,["Doctor","Patient"]))
def details(request,id): 
    queryset = Prescription.objects.filter(ID=id).values()
    return JsonResponse(list(queryset),safe=False)

@login_required
@user_passes_test(lambda u: is_member(u,["Doctor","Patient"]))
def create(request, id):
    context ={}
  
    form = PrescriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
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

