
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name="index"),
   path('Register/',views.register,name="register"),
   path("Management/",views.management,name="management"),
   path("Login/",views.login,name="login"),
   path("Logout/",views.logout,name="logout")

]
