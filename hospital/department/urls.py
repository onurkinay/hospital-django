
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name=""), 
   path('Edit/<int:id>/',views.edit,name="Edit Dept"),
   path('Delete/<int:id>/',views.delete,name="Delete Dept"),
   path('Details/<int:id>/',views.details,name="Details Dept"),
   path('Create/',views.create,name="Create Dept")
]

