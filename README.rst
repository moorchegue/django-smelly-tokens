####################
Django Smelly Tokens
####################

It is sometimes possible to tell that code stinks even without looking at it.
This Django app tries to accomplish that.

.. image:: https://gitlab.com/murchik/django-smelly-tokens/badges/master/build.svg
    :target: https://gitlab.com/murchik/django-smelly-tokens/commits/master
    :alt: Pipeline status

.. image:: https://readthedocs.org/projects/django-smelly-tokens/badge/?version=latest
    :target: https://django-smelly-tokens.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation status


Installation
============

.. code-block:: bash

    pip install django-smelly-tokens


Usage
=====


In your ``settings.py`` define ``SMELLY_TOKENS_APPLICATIONS`` list with
packages you want to inspect.


In a package with code quality tests (e.g. test_tokens.py) import tests you
want to check your apps against:

.. code-block:: python

   from smelly_tokens.test_smelly_tokens import (
       EvalTokenTestCase,
       PdbTokenTestCase,
   )


Run ``django-admin.py test`` or ``./manage.py test`` or ``py.test`` or ``nose``
or whatever runner you're using.


Exceptions
==========

To silence known errors PEP8-style ``noqa`` comment can be used in the
beginning of a file:


.. code-block:: python

   # smelly_tokens: noqa


Or in-line:


.. code-block:: python

   eval('print 123')  # noqa


To exclude an entire directory add it's path to ``SMELLY_TOKENS_EXCLUDE_DIRS``
list in ``settings``.


Adding your own tokens
======================

To create a new type of smelly token test case, inherit
``SmellyTokensTestCase`` and override ``_tokens`` list:

.. code-block:: python

   from django.test import TestCase
   from smelly_tokens.test_smelly_tokens import SmellyTokensTestCase


   class OOPTokensTestCase(SmellyTokensTestCase, TestCase):
   """ OOP hater. """
   _tokens = ['class', 'object', 'Object']


References
==========

* `Full documentation <https://django-smelly-tokens.readthedocs.io/>`__;
