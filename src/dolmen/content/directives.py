# -*- coding: utf-8 -*-

import os.path
import martian
from sys import modules

from dolmen.content.interfaces import IFactory
from martian.directive import StoreOnce
from zope.formlib.form import Fields
from zope.interface import classImplements
from zope.interface.interfaces import IInterface
from zope.interface.advice import addClassAdvisor
from zope.schema.fieldproperty import FieldProperty


class FileValueStoreOnce(StoreOnce):

    def set(self, locals_, directive, value):

        if not os.path.isfile(value):
            pyfile = modules[locals_['__module__']].__file__
            value = os.path.join(os.path.dirname(pyfile), value)
            if not os.path.isfile(value):
                raise martian.error.GrokImportError(
                    "Directive %r cannot resolve the file %r." %
                    (directive.name, value)
                    )
        StoreOnce.set(self, locals_, directive, value)


FILE_PATH_ONCE = FileValueStoreOnce()


def validateSchema(directive, *ifaces):
    for iface in ifaces:
        if not IInterface.providedBy(iface):
            raise martian.error.GrokImportError(
                "%s directive can only use interface classes. "
                "%s is not an interface class. " % (directive.name, iface))


def verifyFactory(directive, factory):
    if factory and not IFactory.implementedBy(factory):
        raise martian.error.GrokImportError(
            "%s directive can only use classes that implement IFactory. "
            "%s is not a valid factory. " % (directive.name, factory))


class schema(martian.Directive):
    scope = martian.CLASS
    store = martian.ONCE
    validate = validateSchema

    def initialize(self, schemas):
        formfields = Fields(*schemas)
        for formfield in formfields:
            fname = formfield.__name__
            if not fname in self.frame.f_locals:
                self.frame.f_locals[fname] = FieldProperty(formfield.field)


    def factory(self, *schemas):
        self.initialize(schemas)
        addClassAdvisor(_schema_advice, depth=3)
        return list(schemas)


def _schema_advice(cls):
    interfaces = schema.bind().get(cls)
    classImplements(cls, *interfaces)
    return cls


class icon(martian.Directive):
    scope = martian.CLASS
    store = FILE_PATH_ONCE
    validate = martian.validateText


class factory(martian.Directive):
    scope = martian.CLASS_OR_MODULE
    store = martian.ONCE
    validate = verifyFactory


class nofactory(martian.MarkerDirective):
    scope = martian.CLASS
    store = martian.ONCE_NOBASE
