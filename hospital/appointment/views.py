#Appointment
from django.shortcuts import render
from .models import Appointment
from .forms import AppointmentForm
# Create your views here.
def home(request):
    return render(request,'appointment/home.html')

def details(request,id): #param id
    return False

def create(request):
    if request.method == "GET":
        # dictionary for initial data with 
        # field names as keys
        context ={}
 
    # add the dictionary during initialization
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            form.save()
         
        context['form']= form
        return render(request, "appointment/create.html", context)
    elif request.method == "POST":
        return False

def edit(request,id):
    if request.method == "GET":
        return render(request,'appointment/edit.html')
    elif request.method == "POST":
        return False

def delete(request):
    return False
