#Doctor
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'doctor/home.html')

def details(request,id): #param id, json return
    return False

def create(request):
    if request.method == "GET":
        return render(request,'doctor/create.html')
    elif request.method == "POST":
        return False

def edit(request,id):
    if request.method == "GET":
        return render(request,'doctor/edit.html')
    elif request.method == "POST":
        return False

def delete(request):
    return False
