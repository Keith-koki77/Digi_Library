# DIGI-LIBRARY
![Screenshot from 2024-02-27 12-02-52](https://github.com/Keith-koki77/Digi_Library/assets/122968859/c92090a0-75aa-42d3-8821-4172d7b23bdc)

## INTRODUCTION
* Digi library is an online platform that is aiming to provide digital access to books that are hard to buy or access.

* Connect with fellow book lovers, share insights, and participate in discussions within our vibrant community. From book clubs to author interviews and literary events, there's always something exciting happening at Digi-Library. Join us and become part of a thriving ecosystem of readers united by a love for the written word. 

* Embark on a journey of discovery, learning, and enrichment with Digi-Library. Sign up now to unlock a world of knowledge, inspiration, and endless possibilities. Your next great read awaits! 


## PROJECT SET-UP
* install virtual environment
```
pip install virtualenv
```

* Create virtual environment
```
virtualenv env
```

* Activate the virtual environment
```
source env/bin/activate
```

* Install django(Python Framework)
```
pip install django
```

* Create django project
```
django-admin startproject library
```

* Run Migrations
```
python manage.py migrate
```

* Create Superuser(Admin user)
```
python manage.py createsuperuser
```

* Run Development Server
```
python manage.py runserver
```

* Database Integration
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'), # For local development, use 'localhost' or '127.0.0.1'
        'PORT': os.environ.get('DATABASE_PORT'), # Default PostgreSQL port is usually '5432'
    }
}

```

## PROJECT ARCHITECTURE
```
The architecture of a Django project typically follows the Model-View-Controller (MVC) pattern, although in Django, it's more accurately described as Model-View-Template (MVT). Here's an overview of the components and their interactions within a Django project:

    Models:
        Models represent the data structure of your application. They define the database schema, including tables, fields, relationships, and constraints.
        Models are typically defined in the models.py files within Django apps.
        Django's ORM (Object-Relational Mapping) facilitates interactions with the database, allowing you to perform CRUD (Create, Read, Update, Delete) operations using Python methods rather than raw SQL.

    Views:
        Views handle the request-response cycle in Django. They receive HTTP requests from clients, process them, and return HTTP responses.
        Views are Python functions or classes that receive a request object and return a response object.
        Views are typically defined in the views.py files within Django apps.
        Views can interact with models to retrieve or manipulate data before rendering a response.

    Templates:
        Templates are used to generate HTML dynamically. They provide the structure and layout for the user interface.
        Templates are typically HTML files with embedded Django template language (DTL) syntax.
        Templates allow for the insertion of dynamic data using template variables and expressions.
        Templates are stored in the templates directory within Django apps.

    URLs:
        URLs map incoming HTTP requests to views in Django. They define the routing logic of the application.
        URLs are typically defined in the urls.py files within Django apps.
        URL patterns are mapped to view functions or classes using regular expressions or path converters.

    Settings:
        Settings define the configuration options for a Django project. They control various aspects such as database settings, middleware, installed apps, static files, and more.
        Settings are typically defined in the settings.py file at the project level.
        Settings can also be divided into multiple files for better organization using the settings module.

    Admin:
        Django provides a built-in administration interface for managing site content. It allows authorized users to perform CRUD operations on models without writing custom views.
        Admin functionality is configured using the admin.py files within Django apps.
        Admin interfaces are automatically generated based on the model definitions.

    Middleware:
        Middleware are hooks that intercept and process HTTP requests and responses. They sit between the server and Django application.
        Middleware can perform tasks such as authentication, session management, request/response modification, and more.
        Middleware are configured in the MIDDLEWARE setting in settings.py.

    Static Files:
        Static files include CSS, JavaScript, images, and other assets used by the application's frontend.
        Static files are typically stored in the static directory within Django apps.
        Django provides a built-in mechanism to serve static files during development and recommends using a separate server or CDN for serving static files in production.

    Forms:
        Forms handle user input and validation in Django. They provide a convenient way to work with HTML forms and perform validation on user-submitted data.
        Forms are typically defined in the forms.py files within Django apps.
        Django provides built-in form classes and validation methods to simplify form handling.

```

