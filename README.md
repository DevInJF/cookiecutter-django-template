# cookiecutter-django-template

## Featuring:

* Django 1.10
* django-debug-toolbar
* django-extensions
* django-compressor and SASS/SCSS
* django-storages for Amazon S3
* 12factor based configuration
* coverage and flake8
* Docker and docker-compose

## Instalation:

    $ cookiecutter https://github.com/dvl/cookiecutter-django-template
    
## Folder structure:

    $ tree projeto
    projeto
    ├── bin
    │   └── gosu-amd64
    ├── bower.json
    ├── docker-compose.yml
    ├── Dockerfile
    ├── entrypoint.sh
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
    ├── Makefile
    ├── manage.py
    ├── package.json
    └── requirements.txt

    6 directories, 18 files

