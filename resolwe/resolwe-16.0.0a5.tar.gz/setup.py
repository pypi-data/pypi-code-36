import os.path
import setuptools

# Get the long description from README.
with open('README.rst', 'r') as fh:
    long_description = fh.read()

# Get package metadata from '__about__.py' file.
about = {}
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, 'resolwe', '__about__.py'), 'r') as fh:
    exec(fh.read(), about)

setuptools.setup(
    name=about['__title__'],
    use_scm_version=True,
    description=about['__summary__'],
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author=about['__author__'],
    author_email=about['__email__'],
    url=about['__url__'],
    license=about['__license__'],
    # Exclude tests from built/installed package.
    packages=setuptools.find_packages(
        exclude=['tests', 'tests.*', '*.tests', '*.tests.*']
    ),
    package_data={
        'resolwe': [
            'flow/executors/requirements.txt',
            'flow/static/flow/*.json',
            'toolkit/processes/**.yml',
            'toolkit/tools/**.py',
        ]
    },
    python_requires='>=3.6, <3.7',
    install_requires=[
        # XXX: Temporarily pin Daphne since the latest version requires
        # asgiref~=3.0 which is incompatible with Channels requirement of
        # asgiref~=2.3
        'daphne~=2.2.0',
        'Django~=1.11.0',
        'djangorestframework~=3.9.0',
        'django-filter~=2.0.0',
        'django-guardian>=1.4.2',
        'django-mathfilters>=0.3.0',
        'django-versionfield2>=0.5.0',
        'django-fernet-fields>=0.5',
        'django-priority-batch>=1.1.0',
        'elasticsearch-dsl~=5.4.0',
        'psycopg2>=2.5.0, <2.8',
        'mock>=1.3.0',
        'PyYAML>=3.11',
        'jsonschema~=2.6.0',
        'Sphinx>=1.5.1, <1.7.0',
        'Jinja2>=2.9.6',
        'wrapt>=1.10.8',
        'shellescape>=3.4.1',
        'asteval~=0.9.12',
        # XXX: Temporarily pin idna since the latest version of the requests
        # package (2.20.1) explicitly requires idna>=2.5,<2.8
        'idna==2.7',
        'redis~=3.2.0',
        'channels~=2.1',
        'channels_redis~=2.3',
        'async-timeout~=2.0',
        'plumbum~=1.6.6',
        'resolwe-runtime-utils>=2.0.1',
    ],
    extras_require={
        'docs': ['sphinx_rtd_theme'],
        'package': ['twine', 'wheel'],
        'test': [
            'check-manifest',
            'coverage>=4.2',
            'pycodestyle~=2.4.0',
            'pydocstyle~=2.1.1',
            'pylint~=1.9.4',
            'readme_renderer',
            'setuptools_scm',
            'testfixtures>=4.10.0',
            'tblib>=1.3.0',
            'isort~=4.3.12',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='resolwe dataflow django',
)
