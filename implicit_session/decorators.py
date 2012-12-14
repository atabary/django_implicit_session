# -*- coding: utf-8 -*-

"""
implicit_session.decorators
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by Alexis Tabary.
:license: Apache2, see LICENSE for more details.

"""

from functools import wraps

from django.contrib.auth import login
from django.utils.decorators import available_attrs

from implicit_session import utils


def implicit_login(view_func):
    """
    Implicitely log a user if required.

    """

    @wraps(view_func, assigned=available_attrs(view_func))
    def _wrapped_view(request, *args, **kwargs):

        # Check whether we need to create a new user
        user = request.user
        if user.is_anonymous():
            # Create and login a new user
            new_user = utils.create_unique_user()
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, new_user)
            # Update the user
            request.user = new_user

        # Call the wrapped function
        return view_func(request, *args, **kwargs)

    return _wrapped_view
