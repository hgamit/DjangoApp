# DjangoApp
Django E-commerce Application

Pre-requisites:
install Python 3.6 https://www.python.org/downloads/, and while installing python choose most of the checkboxes.

Steps to Run App:
1. From command line: pip install virtualenv
3. Change Directory to myTest
4. Run .\Scripts\activate
5. Make sure, nstall required python packages: pip install <PACKAGE_NAME>
   Django==1.10.6
   stripe==1.50.0
   django-allauth==0.31.0
   django-crispy-forms==1.6.1
6. Change Directory to src folder and Run "python manage.py runserver"
7. Check below URL's:
  http://127.0.0.1:8000/
  http://127.0.0.1:8000/admin/
  http://127.0.0.1:8000/checkout/

  
To Check the DB (https://github.com/hgamit/DjangoApp/blob/master/myTest/src/db.sqlite3)

1. Download sqlite from http://www.sqlite.org/2017/sqlite-tools-win32-x86-3170000.zip

2. extract and set the path

3. then go to the <Workarea>\DjangoApp\myTest\src

4. open command prompt

5. > python manage.py dbshell

to view tables use sqlite> .tables

to view schema use sqlite> .schema