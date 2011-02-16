"""
Schema directive
================

  >>> from dolmen.content import schema

  >>> class Test(object):
  ...     pass

  >>> print schema.bind().get(Test)
  None

  >>> inst = Test()
  >>> print schema.bind().get(Test)
  None



  >>> class TestWrongSchema(object):
  ...     schema('toto')
  Traceback (most recent call last):
  ...
  GrokImportError: schema directive can only use interface classes.
  toto is not an interface class.



  >>> from zope.interface import Interface

  >>> class SchemaA(Interface):
  ...     pass

  >>> class SchemaB(Interface):
  ...     pass

  >>> class TestWithSingleSchema(object):
  ...     schema(SchemaA)

  >>> print schema.bind().get(TestWithSingleSchema)
  [<InterfaceClass dolmen.content.tests.schema.directive.SchemaA>]



  >>> class TestWithMultipleSchema(object):
  ...     schema(SchemaA, SchemaB)

  >>> print schema.bind().get(TestWithMultipleSchema)
  [<InterfaceClass dolmen.content.tests.schema.directive.SchemaA>,
   <InterfaceClass dolmen.content.tests.schema.directive.SchemaB>]

"""
