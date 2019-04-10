from setuptools import setup, find_packages


setup(
    name='frasco',
    version='1.2.21',
    url='http://github.com/digicoop/frasco',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description='Set of extensions for Flask to develop SaaS applications',
    packages=find_packages(),
    package_data={
        'frasco': [
            'angular/static/*.js',
            'billing/invoicing/emails/*.html',
            'mail/templates/*.html',
            'mail/templates/layouts/*',
            'templating/*.html',
            'templating/bootstrap/*.html',
            'users/emails/users/*.txt',
            'users/templates/users/*.html'
        ],
    },
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'Flask-Login',
        'Flask-Bcrypt',
        'Flask-Mail',
        'Flask-Babel',
        'Flask-Assets',
        'Flask-WTF',
        'Flask-CORS',
        'Flask-RQ2',
        'psycopg2-binary',
        'PyYAML',
        'jinja-macro-tags',
        'jinja-layout',
        'python-slugify',
        'ago',
        'simplejson',
        'speaklater',
        'requests',
        'apispec',
        'htmlmin',
        'cssmin',
        'jsmin',
        'boto',
        'goslate',
        'premailer',
        'Markdown',
        'inflection',
        'geoip2',
        'redis',
        'python-socketio',
        'eventlet',
        'authlib',
        'stripe',
        'suds',
        'python-dateutil'
    ],
    entry_points='''
        [console_scripts]
        frasco=flask.cli:main
    '''
)
