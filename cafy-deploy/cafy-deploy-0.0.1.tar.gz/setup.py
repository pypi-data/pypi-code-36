import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cafy-deploy",
    version="0.0.1",
    author="Amrendra Kumar",
    author_email="kuamrend@cisco.com",
    description="Cafy deployment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://cafy.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
