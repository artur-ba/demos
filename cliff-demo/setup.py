#!/usr/bin/env python

PROJECT = 'cliffdemo'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Demo app for cliff',
    long_description=long_description,

    author='Artur Basiak',
    author_email='artur.basiak@gmail.com',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'cliffdemo = cliff_demo.main:main'
        ],
        'cliff.cliff_demo': [
            'pycon = cliff_demo.pycon:Pycon',
            'files = cliff_demo.files:Files',
            'hooked = cliff_demo.hooked:Hooked'
        ],
        'cliff.cliff_demo.hooked': [
            'sample-hook = cliff_demo.hooked:Hook'
        ],
    },

    zip_safe=False,
)
