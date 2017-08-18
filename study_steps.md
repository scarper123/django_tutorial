1. install django
    pip install django
2. migrate database
    python manage.py migrate
    In Django, we use migrations to create/alter/delete tables in the database. 
3. start new app
    python manage.py startapp blog
4. Template
    a. Django treats all of the templates directories as a single directory.
    b. Due to this behavior Django recommends creating a subdirectory inside the templates directory by the name of the app.
    c. Order of the dot lookups
        Dictionary lookup - var.['key']
        Attribute lookup - var.key
        Method call lookup - var.key()
        List-index loopup - var.1
    d. Don't be tempted to use parentheses to group expression in the if tag. 
5. View task
    Most of the time a view does the following task:
    1)    Pull data from the database using models.
    2)    Load the template file and create Template object.
    3)    Create Context object to supply data to the template.
    4)    Call render() method
    5)    Create HttpResponse() and send it to the client

6. include other html
    What if include fails to find the template ??
    In that case Django will do one the following two things:
    1) If DEBUG mode is set to True then Django template system will throw TemplateDoesNotExist exception.
    2) If DEBUG is set to False then it will fail silently displaying nothing in the place of include tag.

7. Model
    A Model defines essential fields and behaviors of the data you are storing. In simple words a Model allows us to do following things:
    1) Create tables and define relationship between them.
    2) Modify tables and relationship between them.
    3) Access data stored in tables using Django ORM (without creating raw SQL queries).

8. Model define
    Django automatically adds a primary key field called id for all models, so you don't need to define it manually
    1) Creating one-to-many relationship is simple, just add ForeignKey to the many sides of the relationship (i.e posts) and pass the name of the model you want to connect as a first parameter to ForeignKey constructor.
    2) To create many-to-many relationship add ManyToManyField field to any one side of the realtionship i.e you can add ManyToManyField to either in Tag model or Post model. 

9. Migrations in Django
    Migration is way to create or alter tables in the database. In Django the common workflow of working with models is as follows:
    1) Create or change models in models.py file.
    2) Create migration file.
    3) Commit changes to the database using the migration file created in step 2.

10. Url for template and python code
    1) Template use "{% url "name_of_url_pattern" arg1 arg2 %}"
    2) python code use "reverse(name_of_url_pattern, arg1, arg2)"
    3) common use "get_absolute_url" in template and python code, and it recommand by django.
        a) implement function in the model's class.
        b) use template call or python code call

    command:
        1) python manage.py check
        2) python manage.py makemigrations blog
        3) python manage.py sqlmigrate blog 0001
        4) python manage.py migrate

11. Form Basic
    1) Form states
        a) Unbound state
        b> Bound state
    2) Accessing cleaned data

12. Form and ModelForm
    1) ModelForm allows to connect a Form class to the Model class.

13. Static files

14. Cookie and Session
    1) Cookie communication between browser and server, and data sensitive.
    2) Session save data in server, and use cookie sessionid communication with browser.

Study Link: https://overiq.com/django/1.10/revisiting-cadmin-app/
