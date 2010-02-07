"""
Instanciation
=============

A dolmen.content Content only needs a name to be fully useable.

  >>> mongo = Dummy()
  >>> mongo.__content_type__
  'DummyContent'
  
  >>> from grokcore.component.interfaces import IContext
  >>> IContext.providedBy(mongo)
  True


Schema
======

This content is getting a base interface and a base schema.
It means that the attributes are set by default on the content type.
Of course, the basic fields validations are respected.

  >>> dolmen.IBaseContent.providedBy(mongo)
  True
  >>> mongo.title
  u''
  >>> mongo.title = 'a vast bowl of pus'
  Traceback (most recent call last):
  ...
  WrongType: ('a vast bowl of pus', <type 'unicode'>, 'title')
  
  >>> mongo.title = u'Oh... it makes me mad... mad!'
  >>> mongo.title
  u'Oh... it makes me mad... mad!'


Factory
=======

In order to get an abstract and generic way to handle the content types,
`dolmen.content` provides a factory system that permits to instanciate your
objects.

Further, if no factory is explicitly declared, one is automatically generated
and registered, using the package path and class name as an identifier.

  >>> from dolmen.content import IFactory
  >>> from zope.component import getUtility
  >>> myfactory = getUtility(IFactory,
  ...                        name='dolmen.content.tests.overview.simple.Dummy')
  >>> myfactory.factory
  <class 'dolmen.content.tests.overview.simple.Dummy'>
  >>> myfactory.getSchema()
  [<InterfaceClass dolmen.content.interfaces.IBaseContent>]
"""

import dolmen.content as dolmen

class Dummy(dolmen.Content):
    """A very simple content
    """
    dolmen.name('DummyContent')