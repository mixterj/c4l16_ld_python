import os

from setuptools import setup, find_packages

setup(
    name = "c4l16_ld_python",
    version = "0.1",
    author = "Jeff Mixter and Bruce Washburn",
    author_email = "mixterj@oclc.org washburb@oclc.org",
    description = ("A python script to extract schema.org properties from a URI"),
    license = "Apache License 2.0",
    keywords = "c4l16 rdf",
    url = "https://github.com/mixterj/c4l16_ld_python",
    packages=['parsegraph'],
    install_requires=[
        'rdflib',
        'rdflib-jsonld'
        ],
    entry_points={
        'console_scripts': [
            'parsegraph = parsegraph.__main__:main'
        ]
    }
)
