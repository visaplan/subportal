# -*- coding: utf-8 -*-
from zope.schema.interfaces import (IContextSourceBinder,
     IContextAwareDefaultFactory,
     )
from zope.interface import directlyProvides
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from visaplan.subportal import MessageFactory as _


def possible_subportals(context):
    # for now, use the subportal browser from elsewhere ...
    lst = context.getBrowser('subportal').get_voc_subportals()
    lst = [(tup[1], tup[0])
           for tup in lst
           ]
    voc = SimpleVocabulary.fromItems(lst)
    return voc


def all_subportals(context):
    lst = [tup[0]
           for tup in context.getBrowser('subportal').get_voc_subportals()
           ]
    return lst


def current_subportal_only(context):
    # for now, use the subportal browser from elsewhere ...
    return [context.getBrowser('subportal').get_current_id()]


# TODO: use provider decorator?
# https://docs.plone.org/4/en/external/plone.app.dexterity/docs/reference/dexterity-xml.html
directlyProvides(possible_subportals, IContextSourceBinder)
directlyProvides(all_subportals, IContextAwareDefaultFactory)
directlyProvides(current_subportal_only, IContextAwareDefaultFactory)

