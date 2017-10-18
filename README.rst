.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
visaplan.subportal
==============================================================================

This product is aimed to factor out UNITRACC's subportal feature (which
considers always exactly one of few subportals active, and filters contents by
the subportals which are selected for every content object).

Features
--------

- A behavior to enable subportal support
  (currently dysfunctional because of zcml problem!)
- A schema to provide the subPortal field
- More features yet to transfer here, including the existing "subportal"
  browser


Installation
------------

Install visaplan.subportal by adding it to your buildout::

    [buildout]

    ...
    develop =
        src/visaplan.subportal

    eggs =
        visaplan.subportal


In the src directory, clone the project by::

    git clone https://github.com/visaplan/subportal.git

and then run ``bin/buildout``
