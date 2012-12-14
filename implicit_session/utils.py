# -*- coding: utf-8 -*-

"""
implicit_session.utils
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by Alexis Tabary.
:license: Apache2, see LICENSE for more details.

"""

from django.contrib.auth.models import User
from django.db import IntegrityError


def create_unique_user():
    """
    Recursively try to create a user until an available username is found.

    """
    rnd = User.objects.make_random_password(length=15)
    try:
        return User.objects.create_user(username='__implicit_%s' % rnd)
    except IntegrityError:
        return create_unique_user()
