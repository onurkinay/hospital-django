from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name=""), 
   path('Edit/<int:id>/',views.edit,name="Edit Accountant"),
   path('Edit/',views.edit,name="Edit Accountant logged on"),
   path('Delete/<int:id>/',views.delete,name="Delete Accountant"),
   path('Details/<int:id>/',views.details,name="Details Accountant"),
   path('Create/',views.create,name="Create Accountant")
  
]
