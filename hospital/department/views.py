from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request,'department/home.html')

def details(request): #param id
    return False

def create(request):
    if request.method == "GET":
        return render(request,'department/create.html')
    elif request.method == "POST":
        return False

def edit(request,id):
     return render(request,'department/edit.html')

def delete(request):
    return False


