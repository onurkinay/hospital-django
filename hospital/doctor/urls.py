from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name=""), 
   path('Edit/<int:id>/',views.edit,name="Edit Doctor"),
   path('Delete/<int:id>/',views.delete,name="Delete Doctor"),
   path('Details/<int:id>/',views.details,name="Details Doctor"),
   path('Create/',views.create,name="Create Doctor")
]
