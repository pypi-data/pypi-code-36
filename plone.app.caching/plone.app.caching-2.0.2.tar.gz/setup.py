# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


version = '2.0.2'

setup(
    name='plone.app.caching',
    version=version,
    description='Plone UI and default rules for plone.caching/z3c.caching',
    long_description=(open('README.rst').read() + '\n' +
                      open('CHANGES.rst').read()),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 5.2',
        'Framework :: Zope2',
        'Framework :: Zope :: 4',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='plone caching',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.org/project/plone.app.caching',
    license='GPL version 2',
    packages=find_packages(),
    namespace_packages=['plone', 'plone.app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'six',
        'python-dateutil',
        'plone.caching',
        'plone.cachepurging',
        'plone.app.registry >= 1.0b5',
        'zope.browserresource',
        'zope.interface',
        'zope.component',
        'zope.publisher',
        'zope.pagetemplate',
        'plone.memoize',
        'plone.protect',
        'plone.registry >= 1.0b4',
        'Products.CMFDynamicViewFTI',
        'Products.GenericSetup',
        'Products.CMFCore',
        'Products.statusmessages',
        'Zope2',
        'Acquisition',
        'plone.app.z3cform',
        'plone.z3cform >= 1.1.0.dev0;python_version>"3.0"',
        'z3c.form',
        'z3c.zcmlhook',
    ],
    extras_require={
        'test': [
            'plone.app.contenttypes[test]',
            'plone.app.testing',
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
