#!/usr/bin/env python

"""The setup script."""

ver_globals = {}
with open("ls4gan/version.py") as fp:
    exec(fp.read(), ver_globals)
version = ver_globals["version"]

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="LS4GAN Group",
    author_email='bv@bnl.gov',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python interface to LS4GAN training, tests, data preperation, etc.",
    entry_points={
        'console_scripts': [
            'ls4gan=ls4gan.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ls4gan',
    name='ls4gan',
    packages=find_packages(include=['ls4gan', 'ls4gan.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ls4gan/ls4gan',
    version=version,
    zip_safe=False,
)
