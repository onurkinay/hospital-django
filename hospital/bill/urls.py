
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name=""), 
   path('Edit/<int:id>/',views.edit,name="Edit Bill"),
   path('Delete/<int:id>/',views.delete,name="Delete Bill"),
   path('Details/<int:id>/',views.details,name="Details Bill"),
   path('Payment/<int:id>/',views.payment,name="Pay Bill")
]
