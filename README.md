# ashabaheebwa
Personal Website and blog

This is a personal website(portfolio) and Blog written in Django.

To use as your own just follow the steps below.

# Steps to install and use.

### Clone or Fork

``` $ git clone https://github.com/TrippleA-Ashaba/ashabaheebwa.git ```

or you can fork if you prefer.

### Install Dependencies
``` $ pip install -r requirements.txt ```

### Add evironment variables
create a .env file inside the base directory. ie same level as manage.py
</br>
``` $ touch .env ```

add the following in the .env file
```
<!-- secrets and dev mode -->
SECRET_KEY='MY DJANGO PROJECT SECRET KEY'
DEBUG=True

<!-- email backend for password reset and email sending -->
EMAIL_HOST_PASSWORD = "MY API KEY"
EMAIL_HOST_USER = "USER NAME"

<!-- Database configurations -->
DB_USER='user'
DB_NAME='dbname'
DB_PASSWORD='password'

```
### Create a Mysql DB or use your favorite. 
If you decide to use a different DB, ensure to make changes in the django_project/setting.py file

### Makemigrations and Migrate
populate the database with tables
``` $ python manage.py makemigrations ```
</br>
``` $ python manage.py migrate ```

### Collect static files
``` $ python manage.py collectstatic ```

### Create admin user
``` $ python manage.py createsuperuser ```

### Run server
``` $ python manage.py runserver ```

### Login in to add posts
``` your_domain/admin ```

### Navigations
```your_domain ```    #portifolio page
</br>
``` your_domain/blog ```  #blog page

#ENJOY
