#Patient
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'patient/home.html')

def details(request,id): #param id, json return
    return False

def create(request):
    if request.method == "GET":
        return render(request,'patient/create.html')
    elif request.method == "POST":
        return False

def edit(request,id):
    if request.method == "GET":
        return render(request,'patient/edit.html')
    elif request.method == "POST":
        return False

def delete(request):
    return False
