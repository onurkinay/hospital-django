from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    def ready(self): 
        from django.contrib.auth.models import Group
        
        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='Patient')
        Group.objects.get_or_create(name='Doctor')
        Group.objects.get_or_create(name='Accountant')
      
