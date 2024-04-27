from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name=""), 
   path('Edit/<int:id>/',views.edit,name="Edit Admin"),
   path('Edit/',views.edit,name="Edit Admin logged on"),
   path('Delete/<int:id>/',views.delete,name="Delete Admin"),
   path('Details/<int:id>/',views.details,name="Details Admin"),
   path('Create/',views.create,name="Create admin")
  
]
