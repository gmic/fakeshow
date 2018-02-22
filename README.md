# fakeshow

http://www.fakeshow.nl/ website

# Running gulp

npm install --global gulp-cli

cd fakeshow/static/base_theme
npm install
gulp


# Getting started

* Install python
* Install postgres

Create the user and database in postgres:

    createuser --pwprompt fakeshow-dev
    createdb -Oteamstoer-dev -Eutf8 fakeshow-dev

Create schema's:

    ./manage.py migrate

Run the server:

    ./manage.py runserver
