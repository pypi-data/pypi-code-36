#!/usr/bin/python
from setuptools import setup
import sys
from hszinc import __version__

requirements = [
            'pyparsing',
            'pytz',
            'iso8601',
            'six',
            'pint',
]

setup(name='hszinc',
        url='https://github.com/vrtsystems/hszinc',
        description='Parser and dumper for Project '\
                    'Haystack ZINC (Zinc is not CSV) file format',
        version=__version__,
        author='VRT Systems',
        author_email='support@vrt.com.au',
        license='BSD',
        packages=[
            'hszinc',
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: No Input/Output (Daemon)',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Information Analysis',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        requires=requirements,
        install_requires=requirements
)
