# cookiecutter-django-clean-template

## Featuring:

* Django 1.9
* django-debug-toolbar
* django-extensions
* django-compressor and SASS/SCSS
* 12factor based configuration
* coverage and flake8
* bower
* Docker and docker-compose

## Instalation:

    $ cookiecutter https://github.com/dvl/cookiecutter-django-clean-template
    
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

