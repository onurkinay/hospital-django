#Appointment
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'appointment/home.html')

def details(request,id): #param id
    return False

def create(request):
    if request.method == "GET":
        return render(request,'appointment/create.html')
    elif request.method == "POST":
        return False

def edit(request,id):
    if request.method == "GET":
        return render(request,'appointment/edit.html')
    elif request.method == "POST":
        return False

def delete(request):
    return False
