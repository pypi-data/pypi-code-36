import json
import os
from setuptools import setup
import io

with open(os.path.join('musicfox_dash_components', 'package.json')) as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

with io.open(os.path.join('.', 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

repo_url = f"https://github.com/thinkjrs/musicfox-dash-components"
setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    packages=[package_name],
    include_package_data=True,
    license=package['license'],
    description=package['description'] if 'description' in package else package_name,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'pandas', 'numpy', 'dash',
    ],
    classifiers = [
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Office/Business',
        'Topic :: Office/Business',
        'Topic :: Office/Business',
        'Topic :: Office/Business',
        'Topic :: Office/Business',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: End Users/Desktop',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: JavaScript',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    url = repo_url,
    
)
