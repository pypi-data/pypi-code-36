import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rbpy-rb',
    version='0.1.2',
    scripts=['rbpy'],
    author='Woodcarver',
    author_email='batpepastrama@gmail.com',
    description='ReaderBench library written in python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://git.readerbench.com/ReaderBench/Readerbench-python',
    packages=setuptools.find_packages(),
    install_requires=[
          'spacy',
          'nltk',
          'gensim',
          'numpy',
          'wget',
          'pymorphy2',
          'xx_ent_wiki_sm'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ],
)
