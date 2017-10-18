# -*- coding: utf-8 -*- äöü
"""Behaviors for Unitracc's Subportals

"""
from Products.CMFCore.interfaces import IDublinCore
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider

from Products.unitracc.tools.debug2 import pp

from visaplan.subportal import MessageFactory as _
from .vocabularies import (
     possible_subportals, current_subportal_only,
     )


@provider(IFormFieldProvider)
class ISubportalSupport(model.Schema):
    """
    Add the subPortals
    """
    subPortals = schema.List(
        title=_('Subportals'),
        value_type=schema.Choice(source=possible_subportals,
                                 title=_('Subportals')),
        defaultFactory=current_subportal_only,
        required=False)


@implementer(ISubportalSupport)
class SubportalSupport(object):
    """
    A class to provide support for Unitracc subportals
    """

    def get_sub_portals(self):
        """
        für Katalog-Index
        """
        val = self.getSubPortals()
        pp(val=val)
        return val

