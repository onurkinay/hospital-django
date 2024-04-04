
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name=""), 
   path('Edit/<int:id>/',views.edit,name="Edit Prescription"),
   path('Delete/<int:id>/',views.delete,name="Delete Prescription"),
   path('Details/<int:id>/',views.details,name="Details Prescription"),
   path('Create/<int:id>/',views.create,name="Create Prescription")
]
