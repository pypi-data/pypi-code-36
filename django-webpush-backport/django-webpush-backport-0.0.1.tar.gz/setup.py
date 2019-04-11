import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-webpush-backport',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GNU Public License',
    description='A simple Django 1.9 package to integrate Web Push Notification in your Application',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://www.github.com/yoitsdave/django-webpush',
    author='Judah Levy',
    author_email='judahjlevy@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'pywebpush==1.6.0'
    ]
)
