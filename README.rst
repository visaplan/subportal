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


Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install visaplan.subportal by adding it to your buildout::

    [buildout]

    ...

    eggs =
        visaplan.subportal


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/sup.BetonQuali/issues
- Source Code: https://github.com/collective/sup.BetonQuali
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
