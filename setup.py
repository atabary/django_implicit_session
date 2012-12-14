#!/usr/bin/env python

import implicit_session

from setuptools import setup, find_packages

setup(
    name='django_implicit_session',
    version=implicit_session.__version__,
    description='Provides a decorator to automatically login anonymous users accessing the specified view in Django.',
    long_description=open('README.rst').read(),
    author='Alexis Tabary',
    author_email='alexis.tabary@gmail.com',
    url='https://github.com/atabary/django_implicit_login',
    packages=find_packages(),
    license=open('LICENSE').read(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
