# -*- coding: utf-8 -*-
"""Installer for the visaplan.subportal package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='visaplan.subportal',
    version='0.1',
    description="Unterstützung für Unitracc-Subportale",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Tobias Herp',
    author_email='tobias.herp@stein.de',
    # url='https://pypi.python.org/pypi/visaplan.subportal',
    url='svn+ssh://svn.visaplan.com/unitracc/products/visaplan.subportal/trunk',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['visaplan'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # Dexterity-Projekt-Generierung:
        'plone.app.dexterity [grok]',
        'plone.namedfile [blobs]',
        # weitere:
        'plone.behavior', 
        'zope.schema', 
        'zope.interface', 
        'zope.component', 
        'Products.CMFCore',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
