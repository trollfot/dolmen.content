# -*- coding: utf-8 -*-

from dolmen.content import interfaces
from dolmen.content.directives import schema
from grokcore.component import baseclass
from grokcore.content import Model, Container, OrderedContainer
from zope.dublincore.property import DCProperty
from zope.interface import implements


class BaseContent(Model):
    baseclass()
    schema(interfaces.IBaseContent)

    title = DCProperty('title')


class Container(BaseContent, Container):
    """A dolmen folderish content type.
    """
    baseclass()
    implements(interfaces.IContainer)


class OrderedContainer(BaseContent, OrderedContainer):
    """A dolmen folderish content type with ordered keys.
    """
    baseclass()
    implements(interfaces.IOrderedContainer)


class Content(BaseContent):
    """A dolmen content type.
    """
    baseclass()
    implements(interfaces.IContent)
