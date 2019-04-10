import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="obp_python",
    version="0.1",
    author="",
    author_email="",
    description="Beta Open Bank Project Python Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrisjsimpson/open-bank-project-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    install_requires=['click', 'requests', 'appdirs'],
    entry_points='''
      [console_scripts]
      obp=obp_python:cli
    ''',
)
