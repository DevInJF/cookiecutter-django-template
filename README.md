# cookiecutter-django-clean-template

## Featuring:

* Django 1.9
* django-debug-toolbar
* django-extensions
* django-compressor and SASS/SCSS
* 12factor based configuration
* bower
* Docker and docker-compose

## Instalation:

    $ cookiecutter https://github.com/dvl/cookiecutter-django-clean-template
    
## Usage:

#### With Docker

    $ cd my-project
    $ make install
    ** wait **
    $ make up
    
#### And without it...

    $ cd my-project
    $ cp .env-example .env
    ** configure your database and put it in `.env` file. **
    $ python manage.py migrate
    ** install node.js and bower if you don't have it already. **
    $ bower install
    
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

