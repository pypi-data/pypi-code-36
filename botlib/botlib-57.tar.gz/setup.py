#!/usr/bin/env python3

""" setup.py """

from setuptools import setup

setup(
    name='botlib',
    version='57',
    url='https://bitbucket.org/bthate/botlib',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description="Framework to program bots",
    long_description=""" BOTLIB is a pure python3 framework to program bots (a botlib), provides IRC and XMPP bots and is extendible  by programming your own commands. 
                         Basic functionality is a RSS feed fetcher you can use to display feeds into your channel. 
                         BOTLIB uses a timestamped, type in filename, JSON stringified, files on filesystem backend and has timed based logging capabilities.
                         BOTLIB has been placed in the Public Domain and contains no copyright or LICENSE
                     """,   
    license='Public Domain',
    install_requires=["obj"],
    packages=["bot"],
    scripts=["bin/bot", "bin/bot-stop"],
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python'
                ]
)
