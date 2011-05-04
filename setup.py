from setuptools import setup, find_packages
from os.path import join

name = 'dolmen.content'
version = '2.0a1'
readme = (open(join('src', 'dolmen', 'content', 'README.txt')).read() + '\n' +
          open(join('src', 'dolmen', 'content', 'test_main.txt')).read())
history = open(join('docs', 'HISTORY.txt')).read()

install_requires = [
    'ZODB3 >= 3.10',  # Persistent.
    'dolmen.container',
    'dolmen.field >= 0.3',
    'grokcore.component >= 2.2',
    'grokcore.security',
    'martian >= 0.12',
    'setuptools',
    'zope.component',
    'zope.i18nmessageid',
    'zope.interface',
    'zope.schema',
    ]

tests_require = [
    'zope.location',
    'zope.testing',
    ]

setup(name = name,
      version = version,
      description = 'Dolmen content type framework',
      long_description = readme + '\n\n' + history,
      keywords = 'Grok Zope3 CMS Dolmen Content',
      author = 'Souheil Chelfouh',
      author_email = 'souheil@chelfouh.com',
      url = 'http://gitweb.dolmen-project.org/',
      download_url = '',
      license = 'GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages = ['dolmen'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      tests_require = tests_require,
      install_requires = install_requires,
      extras_require = {'test': tests_require},
      classifiers = [
        'Environment :: Web Environment',
        'Framework :: Zope3',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
)
