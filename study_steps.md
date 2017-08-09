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


Study Link: https://overiq.com/django/1.10/loading-templates-in-django/
Current page: Loading Templates in Django
