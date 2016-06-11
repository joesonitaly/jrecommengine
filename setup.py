import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="jrecommengine",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    license="BSD License",
    description="A collaborative-filtering recommendation engine.",
    long_description=README,
    url="https://github.com/joesonitaly/jrecommengine",
    author="Joseph O. Onyewuche",
    author_email="joesonitaly@gmail.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.9"
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License"
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
