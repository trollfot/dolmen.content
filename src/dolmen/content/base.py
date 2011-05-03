# -*- coding: utf-8 -*-
import persistent

from dolmen.content import interfaces, require
from dolmen.content.directives import schema, Fields
from dolmen.container.contained import Contained
from dolmen.container.components import BTreeContainer, OrderedBTreeContainer
from grokcore.component import baseclass
from grokcore.component.interfaces import IContext
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.interface import implements


class Content(Contained, persistent.Persistent):
    baseclass()
    require("zope.ManageContent")

    implements(IAttributeAnnotatable, IContext, interfaces.IContent)

    def __init__(self, **kwargs):
        Contained.__init__(self)
        persistent.Persistent.__init__(self)
        if kwargs:
            schemas = schema.bind().get(self)
            if schemas:
                ifields = Fields(*schemas)
                for key, value in kwargs.items():
                    ifield = ifields.get(key)
                    if ifield is None:
                        continue
                    field = ifield.bind(self)
                    field.validate(value)
                    field.set(self, value)


class Container(Content, BTreeContainer):
    """A dolmen folderish content type.
    """
    baseclass()
    implements(interfaces.IContainer)

    def __init__(self, **kwargs):
        BTreeContainer.__init__(self)
        Content.__init__(self, **kwargs)


class OrderedContainer(Content, OrderedBTreeContainer):
    """A dolmen folderish content type with ordered keys.
    """
    baseclass()
    implements(interfaces.IOrderedContainer)

    def __init__(self, **kwargs):
        OrderedBTreeContainer.__init__(self)
        Content.__init__(self, **kwargs)
