# -*- coding: utf-8 -*-

from grokcore.component import zcml
from zope.configuration.config import ConfigurationMachine


def grok(*module_name):
    config = ConfigurationMachine()
    zcml.do_grok('zope.component', config)
    zcml.do_grok('grokcore.component.meta', config)
    for mn in module_name:
        zcml.do_grok(mn, config)
    config.execute_actions()
