# E-commerce Project - Best Bargain

An e-commerce web app which advertises products using affiliate links. The website includes a Blog, Stripe Payments & User Authentication. This app was created as a final project for Code Institute's bootcamp course and was used for that purpose. It was built using Python's Django Framework.

No template was used.

## Demo

To view the live version of this website please follow this link https://ecommerce-affiliate-project.herokuapp.com/

## Installation

1. Firstly you will need to clone this repository by running the git clone ```https://github.com/rcomiskey/ecommerce_project``` command
2. Create a virtual environment ``$ python3 -m venv ~/virtualenvs/<environment name>``
3. Then activate it with command ``$ source ~/virtualenvs/<environment name>/bin/activate``
4. Install dependencies ``$ sudo pip3 install -r requirements.txt``
5. At the top level, create a file named 'environment.sh' and add the code below into it
```
export SECRET_KEY=""

export STRIPE_PUBLISHABLE=""

export STRIPE_SECRET="" 

```
6. Obtain a secret key from [Mini Web Tool](https://www.miniwebtool.com/django-secret-key-generator/) 
7. Create a [Stripe](https://stripe.com/ie) account and navigate to the API section to find the STRIPE_PUBLISHABLE and STRIPE_SECRET keys
8. Add the keys to 'environment.sh'
9. To run locally, the default sqlite database can be used with the following changes to settings.py
 
Replace:
```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3"))
}
```
With:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```


10. To use a different database, leave the code the same and add the following (including the database url) to 'environment.sh'
```
export DATABASE_URL=''
```

11. The settings.py will also need to be altered depending on how you are running it. Follow the guide below

*Leave this code to run locally or comment out if deploying to a host*
```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
```

*Leave this code if deploying to a host or comment out if running locally*
```
if USE_S3:
    AWS_S3_OBJECT_PARAMETERS = {  
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    
    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'


```

12. Then run command ```$ python3 manage.py migrate```
13. Create an admin account, enter command ```$ python3 manage.py createsuperuser``` and complete details
14. Start the development server with command ```$ python3 manage.py runserver```
15. Open your browser and enter '127.0.0.1:8000' to view the app

## Built With
- HTML5
- CSS3
- Python
- Bootstrap
- Postgres 
- Django Framework

##### Hosted on Heroku and Amazon S3 bucket hosts the static files 

## Apps

### accounts
The purpose of this app is user authentication. It renders 3 templates,"register.html", "login.html" and "profile.html",  which allows user to sign up, login and view there details on a profile page.

### blog
The blog app allows admin to create posts for the user to view. The user also has the ability to comment on each individual blog post. There is a newsletter sign up form in the blog app which allows the user to subscribe with a once of payment using stripe.

### products
This app has several functions involving products. 
- First of all there is a python script (products/management/commands/loadSampleData.py) which allows admin to import products by entering the command ```python3 manage.py loadSampleData --file datafiles/<file name>```, loading a formatted file from 'datafiles'.
- It renders products and categories.
- Each product has a 'deep link' which bring the user directly to a merchants product page. It runs through the "selected_product" function in product.views.py before redirecting.

### search
The search app allows the user to input a keyword to find products rendered via 'viewproduct.html'.

### viewed
Once logged in, the viewed app captures the history of a users clicked products.

## Testing

Django’s unit tests use a Python standard library module(unittest), it defines tests using a class-based approach.

Tests were created in 3 apps:

1. ##### accounts 
- A test to check that a new user can successfully register
- The second test to confirm the registration form fails when an email is not entered

2. ##### blog
- Testing that the correct http respose code is returned for the url and that the "blogposts.html" template is rendered

3. ##### products
- This test that the view "viewproducts" resolves

To run tests, use the command ```python3 manage.py test <name of app>```

