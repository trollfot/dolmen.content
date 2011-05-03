import dolmen.content as dolmen
from dolmen.content import testing
from grokcore.component import baseclass
from dolmen.container.components import Container
from zope.interface import Interface
from zope.schema import TextLine
from zope.testing.cleanup import cleanUp


class IMythologicalHero(Interface):
    """A hero that transcended History.
    """
    homecity = TextLine(
        title=u"Name of the home city of the Hero",
        required=True,
        default=u"Babylon")


class Hero(dolmen.Content):
    baseclass()
    dolmen.schema(IMythologicalHero)


class AssyrianHero(Hero):
    baseclass()


class MesopotamianGod(Container, AssyrianHero):
    pass


def setup_module(module):
    """ grok the publish module
    """
    testing.grok("dolmen.content.meta",
                 "dolmen.content.tests.schema.test_heritage")


def teardown_module(module):
    """ undo groking
    """
    cleanUp()


def test_inheritage():
    """Test that hineritance keeps schema"""

    gilgamesh = MesopotamianGod()
    assert gilgamesh.homecity == u'Babylon'
    assert dolmen.schema.bind().get(gilgamesh) == [IMythologicalHero, ]
