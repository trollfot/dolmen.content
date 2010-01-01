from setuptools import setup, find_packages
from os.path import join

name = 'dolmen.content'
version = '0.3'
readme = open(join('src', 'dolmen', 'content', 'README.txt')).read()
history = open(join('docs', 'HISTORY.txt')).read()

install_requires = [
    'dolmen.field>=0.3',
    'grok',
    'grokcore.component',
    'grokcore.security',
    'martian',
    'setuptools',
    'zope.annotation',
    'zope.component',
    'zope.dublincore',
    'zope.formlib',
    'zope.i18nmessageid',
    'zope.interface',
    'zope.schema',
    ]

tests_require = [
    'zope.testing',
    'zope.app.testing',
    'zope.app.zcmlfiles',
    ]

setup(name = name,
      version = version,
      description = 'Dolmen content-type framework',
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
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Zope3',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
)
