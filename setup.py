"""Setup for titanic-ds."""
from setuptools import setup, find_packages

setup(
    name='titanic-ds',
    version='0.0.1',
    description='A package predict whether of not a person would survive the Titanic',
    url='https://github.com/Seb-Good/titanic-ds.git',
    author='Sebastian D. Goodfellow',
    author_email='sebi.goodfellow@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='machine learning titanic',
    python_requires='>=3.5',
    entry_points={
        'console_scripts': ['titanic-ds = src.predict:main'],
        },
    install_requires=[]
)