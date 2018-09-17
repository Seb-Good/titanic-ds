"""Setup for titanic-ds."""
from setuptools import setup, find_packages

setup(
    name='titanic-ds',
    version='0.0.1',
    description='A package to predict whether or not a person would survive the Titanic',
    url='https://github.com/Seb-Good/titanic-ds.git',
    author='Sebastian D. Goodfellow',
    author_email='sebi.goodfellow@gmail.com',
    license='MIT',
    keywords='machine learning titanic',
    package_dir = {'': 'titanic'},
    packages=find_packages('titanic', exclude=['tests']),
    zip_safe=False,
    test_suite='tests',
)
