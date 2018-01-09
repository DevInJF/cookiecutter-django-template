# {{ cookiecutter.project_name }}

This project is pre-configured with some facilities for a quick project start using Django.

## Requisites
* [Pipenv](https://docs.pipenv.org/)
* [NPM](https://nodejs.org/en/)
* [PostgreSQL](https://postgresapp.com/)

Pipenv should be able to configure the whole project since the installation of the required Python version, virtualenv creation and the packages used by the project itself.

## Installation

    $ cp .env-example .env
    $ pipenv install --ignore-pipfile
    $ npm install
    
Make sure you have edited the `.env` file according your local environment, then you should be able to run the project.

## Running

Active the virtualenv with the following command

    $ pipenv shell

And then run the development server

    $ python manage.py runserver

That's all
