Django People
=============

A simple app to show person profiles, for example for the "About us" section
of a website.

Comes with a django-cms plugin and is multilingual.


Installation
------------

If you want to install the latest stable release from PyPi::

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


