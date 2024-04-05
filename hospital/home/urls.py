
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name="index"),
   path('Register/',views.register,name="register"),
   path("Login/",views.login,name="login")
]
