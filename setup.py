import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

requires = [
    'bcrypt',
    'blinker',
    'mongoengine',
    'nose2',
    'cov-core'
]

setup(
    name='Stackcite Database',
    version='0.0',
    description='A database library for Stackcite services.',
    long_description=README + '\n\n' + CHANGES,
    author='Konrad R.K. Ludwig',
    author_email='konrad.rk.ludwig@gmail.com',
    url='http://www.konradrkludwig.com/',
    packages=['stackcite'],
    namespace_packages=['stackcite'],
    package_data={'stackcite': ['data/json/*.json', 'data/testing/data/*.json']},
    install_requires=requires
)
