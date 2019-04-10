from setuptools import setup, find_packages

readme = open('README.md').read().strip()

setup(
    name='dtest-framework',
    version='0.1.5',
    license='MIT',
    author='Seth Jensen',
    author_email='sjensen85@gmail.com',
    url='https://github.com/sjensen85/dtest',
    description='A library to facilitate the testing of data inside data pipelines. Results are pushed to a messaging queue of some sort for consumption by applications, persistence, etc.',
    long_description=readme,
    packages=find_packages(),
    install_requires=[
        # put packages here
        'six',
        'pika==1.0.0',
        'pyhamcrest'
    ],
    test_suite='tests',
    entry_points={}
)
