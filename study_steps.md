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

Study Link: https://overiq.com/django/1.10/template-inheritance-in-django/
