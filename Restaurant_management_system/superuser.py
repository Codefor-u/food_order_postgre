from django.contrib.auth.models import User

try:
    User.objects.create_superuser('gaalav', 'codeforyu@gmail.com', 'gaalav321')
    print('Admin user created successfully.')
except Exception as e:
    print('Error creating admin user:', str(e))
