#Bills
from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request,'bill/home.html')

def details(request): #param id
    return False

def create(request):
    if request.method == "GET":
        return render(request,'bill/create.html')
    elif request.method == "POST":
        return False

def edit(request,id):
     return render(request,'bill/edit.html')

def delete(request):
    return False

def payment(request, id):
    return False
