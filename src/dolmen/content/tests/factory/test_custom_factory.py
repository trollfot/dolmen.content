"""
First grok::

  >>> import dolmen.content.testing
  >>> dolmen.content.testing.grok('dolmen.content.meta',
  ...                       'dolmen.content.tests.factory.test_custom_factory')

Custom factories
================

Explicitly linked factories are registered normally::

  >>> from zope.component import getUtility, queryUtility
  >>> from dolmen.content.interfaces import IFactory
  >>> joe = getUtility(IFactory, 'baker_joe')
  >>> isinstance(joe, BakerJoe)
  True

  >>> joe.title
  u"Joe's bakery"
  >>> joe.description
  u'I am a totally custom factory.'

Factories that are not linked with the `factory` directive or by
natural association are disregarded::

  >>> steve = queryUtility(IFactory, 'baker_steve')
  >>> steve is None
  True

"""

import dolmen.content as dolmen
from zope.interface import Interface, implements


class IBread(Interface):
    pass


class BakerJoe(dolmen.Factory):
    dolmen.name('baker_joe')
    title = u"Joe's bakery"
    description = u"I am a totally custom factory."


class BakerSteve(dolmen.Factory):
    dolmen.name('baker_steve')
    title = u"Steve and Sons."


class Baguette(dolmen.Content):
    """A crusty bread.
    """
    dolmen.name(u'White fresh bread')
    dolmen.factory(BakerJoe)
    implements(IBread)
