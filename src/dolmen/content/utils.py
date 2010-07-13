# -*- coding: utf-8 -*-

from dolmen.content import IBaseContent


def get_content_type(component):
    return getattr(component, '__content_type__', None)
