# cookiecutter-django-template

## Features:

* Django 2
* django-debug-toolbar
* django-extensions
* django-compressor and SASS/SCSS
* django-storages for Amazon S3
* 12factor based configuration

## Instalation:

    $ cookiecutter https://github.com/dvl/cookiecutter-django-template

## Folder structure:

    $ tree projeto
    projeto
    ├── projeto
    │   ├── core
    │   │   ├── __init__.py
    │   │   ├── middleware.py
    │   │   └── storages.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── static
    │   │   └── sass
    │   │       └── app.sass
    │   ├── templates
    │   │   └── base.html
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── package.json
    └── requirements.txt

    6 directories, 18 files

