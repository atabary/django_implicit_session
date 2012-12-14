django_implicit_session
=======================

Provides a decorator to automatically login anonymous users accessing the specified view in Django.

It is useful if you need you want to make a "StackOverflow-like" login process where users:

- can start using your service with a persistent session without having registered yet,
- can then convert this implicit session in an explicit one with proper credentials.

It is meant to be used with Django SessionMiddleware, using cookies for authentication. Of course if the user reset his/her cookies, the session will be permanently lost.

Usage
-----

``@implicit_login`` is a very simple wrapper that should be used around views:

.. code-block:: pycon

    from implicit_session import implicit_login

    @implicit_login
    def my_view(request):
        ...

How Does It Work?
-----------------

The decorator checks whether the visitor requesting the view is anonymous or not.

If the visitor is anonymous a new user is created in the database, with a username similar to ``__implicit_2mCvZUEWumDaT9a``, where ``2mCvZUEWumDaT9a`` is generated randomly. The visitor is then automatically logged in with this implicit username.

TODO
----

- Helpers to allow a user to convert his/her implicit session in an explicit one.
