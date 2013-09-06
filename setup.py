import os
from setuptools import setup, find_packages
import people as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-people-academic",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, cms, plugin, people, person, profile',
    author='Liam Jongsu Kim',
    author_email='jskim.cfd@gmail.com',
    url="https://github.com/appleparan/django-people-academic",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.4.3',
        'South',
        'django-libs',
        'django-cms',
        'django-filer',
        'simple-translation',
        'Pillow',
        'django-localized-names',
    ],
    tests_require=[
        'fabric',
        'factory_boy',
        'django-nose',
        'coverage',
        'django-coverage',
        'mock',
    ],
)
