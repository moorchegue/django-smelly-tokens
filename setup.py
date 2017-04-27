#!/usr/bin/env python
import os
from setuptools import setup, find_packages

__doc__ = "Code quality tests"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


readme = read('README.rst')
changelog = read('CHANGELOG.rst')
version = read('VERSION')

setup(
    name='django-smelly-tokens',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + changelog,
    author='murchik',
    author_email='murchik@protonmail.com',
    url='https://github.com/moorchegue/django-smelly-tokens',
    packages=[package for package in find_packages()
              if package.startswith('smelly_tokens')],
    install_requires=[
        'Django>=1.4',
        'pytest-django',
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=[
        'django-setuptest',
    ],
    license="GPLv3",
    zip_safe=True,
    keywords='django-smelly-tokens',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
