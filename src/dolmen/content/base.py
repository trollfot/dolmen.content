# -*- coding: utf-8 -*-

import grok
from dolmen.content import interfaces
from dolmen.content.directives import schema, icon
from zope.dublincore.property import DCProperty


class BaseContent(grok.Model):
    icon('generic.png')
    schema(interfaces.IBaseContent)
    grok.baseclass()

    title = DCProperty('title')


class Container(BaseContent, grok.Container):
    """A dolmen folderish content type.
    """
    grok.baseclass()
    grok.implements(interfaces.IContainer)


class OrderedContainer(BaseContent, grok.OrderedContainer):
    """A dolmen folderish content type with ordered keys.
    """
    grok.baseclass()
    grok.implements(interfaces.IOrderedContainer)


class Content(BaseContent):
    """A dolmen content type.
    """
    grok.baseclass()
    grok.implements(interfaces.IContent)
