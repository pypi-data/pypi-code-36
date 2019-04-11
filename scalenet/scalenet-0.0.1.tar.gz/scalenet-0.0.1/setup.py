import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scalenet",
    version="0.0.1",
    author="Sergiy Popovych",
    author_email="sergiy.popovich@gmail.com",
    description="A universal pytorch module for implementing multiscale architectures (UNet, spatial pyramid, SpyNet, res-Unet)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/supersergiy/scalenet",
    packages=setuptools.find_packages(),
)
