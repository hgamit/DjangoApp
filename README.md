# DjangoApp
Django Application

Pre-requisites:
install Python 3.6 https://www.python.org/downloads/, and while installing python choose most of the checkboxes.

Steps to Run App:
1. From command line: pip install virtualenv
2. virtualenv <NAME_OF_ENV>
3. Change Directory to NAME_OF_ENV
4. Run Scripts\activate
5. Copy src and static folder from here to NAME_OF_ENV directory
6.Install required python packages: pip install <PACKAGE_NAME>
  Django==1.10.6
  stripe==1.50.0
  django-allauth==0.31.0
  django-crispy-forms==1.6.1
7. Change Directory to src folder and Run "python manage.py runserver"
8. Check below URL's:
  http://127.0.0.1:8000/
  http://127.0.0.1:8000/admin/
  http://127.0.0.1:8000/checkout/
9. Create SuperUser:
(myvenv) ~/djangogirls$ python manage.py createsuperuser
Username: admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
