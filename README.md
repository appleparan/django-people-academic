It's Experimental!!
=================


Django People For Academic
=========================
A simple app to show person profiles, for example for the "About us" section
of a website.

Comes with a django-cms plugin and is multilingual.

Assume that you are using bootstrap (>=3.0). 


Requirements
------------
pip install requirements automatically, but you should add following things to your project's settings.py

django>=1.4.3
django-libs
django-cms==3.0b2
django-wysiwyg
django-ckeditor
django-hvad
Pillow>=1.7.8
South>=0.7.6



Installation
------------

If you want to install the latest stable release from PyPi:: (not uploaded yet)

    $ pip install django-people-academic

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/appleparan/django-people-academic.git#egg=people_academic

Add ``people`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'people_academic',
    )

Run the South migrations::

    ./manage.py migrate people_academic


Usage
-----

Use the Django admin to create your person objects. If you are using django-cms
you can use the ``Person Plugin`` to display a person in your placeholders.


