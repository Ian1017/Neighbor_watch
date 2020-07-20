# Neighour-Hood Watch
A web application that allows you to be in the loop about everything happening in your neighborhood.

## Author and contact details
*Ian Mdawida
Email: mdawidamengo@gmail.com

# Project Description
A user of the application should be able to:

1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the health department and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.
A search functionality is implemented where one can search for the different businesses and their images.

# SetUp and installation requirements
You need to have the following installed:
* Python3+
* Pip ```curl https://bootstrap.pypa.io/get-pip|python```
* Virtual ```$ python3.6 -m venv pip virtual```
* Activate the virtual environment ```source virtual/bin/activate```
* Django==1.11 ```(virtual)$ pip install django==1.11```
* Get all requirements ```pip freeze > requirements.txt```

### Setting up the database
The database in use for this project is Postgres
* Ensure postgress is installed. ``` $ sudo apt-get update```
* Step 2 ```sudo apt-get install postgresql postgresql-contrib```

## Connect to postregsql
* ``` $ sudo su - postgres```
* ``` $ psql ```

## Set up the database to the django application
In the settings.py file,

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neighbourhood',
        'USER': '< your postgres user name>',
        'PASSWORD': '< the database password>'
    }
}

### Run migrations
``` $ python manage.py makemigrations ```
``` $ python manage.py migrate ```
### Running the server
```python manage.py runserver```
# Behaviour Driven Development
Some of the behaviours in this application include;
| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Launch the site | User has to login or sign up before using the application | User is updated |
| Login | User is directed to create profile page | user is logged in |
| Create profile | Profile is updated and hood updated | users details are stored. |
| User can only view their hood details | User can change hood detaols in the app | Hood details are displayed|
| Add business | User can add business in different neighbourhoods | Business is added and displayed on homepage|
| Post a notice | Notice displayed can only be viewed by the users of that neighbourhood | neighbours are updated in the neighbourhood|
## Technologies used
* Django a python frame-work
* Javascript
* Html
* Bootstrap
* Python

##LICENSE
[MIT]