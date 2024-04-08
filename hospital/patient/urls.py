
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name=""), 
   path('Edit/<int:id>/',views.edit,name="Edit Patient"),
   path('Edit/',views.edit,name="Edit Patient logged on"),
   path('Delete/<int:id>/',views.delete,name="Delete Patient"),
   path('Details/<int:id>/',views.details,name="Details Patient")
]
