
from django.urls import path
from . import views


urlpatterns = [
   path('',views.home,name=""),
   path('Create',views.create,name="Create Appointment"),
   path('Edit/<int:id>/',views.edit,name="Edit Appointment"),
   path('Delete/<int:id>/',views.delete,name="Delete Appointment"),
   path('Details/<int:id>/',views.details,name="Details Appointment")
]
