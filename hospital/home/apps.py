from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    def ready(self): 
        from datetime import date
        from django.contrib.auth.models import Group,User
        from administrator.models import Administrator
        
        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='Patient')
        Group.objects.get_or_create(name='Doctor')
        Group.objects.get_or_create(name='Accountant')
        if Administrator.objects.all().count() == 0:
            #ilk admin üret
            user = User.objects.create_user(username="admin@hospital.com",
                                    email="admin@hospital.com",
                                    password="123456",first_name="Admin",last_name="Hospital")
            user.save()

            my_group = Group.objects.get(name='Admin')
            my_group.user_set.add(user)

            admin = Administrator.objects.create(User=user,DateOfBirth=date.today(),Gender="M",Phone="+9055555")
            admin.save()




      
