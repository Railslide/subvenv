#!/usr/bin/env python
# coding=utf-8

import codecs
import os
import re
from setuptools import setup, find_packages


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
INIT_PATH = os.path.join("subvenv", "__init__.py")


def read(*path_parts):
    """
    Build an absolute path from *path_parts* and and return the contents
    of the resulting file. Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(ROOT_DIR, *path_parts), "rb", "utf-8") as f:
        return f.read()


def get_readme_content(readme='README.md'):
    """
    Convert *readme* content from markdwon to rst and return it.
    In case of errors, return it as markdown.
    """
    try:
        import pypandoc
        return pypandoc.convert(readme, 'rst')
    except (IOError, ImportError):
        return read(readme)


def get_version():
    """ Extract version from __init__.py """
    version_match = re.search(
        r'^__version__ = [\'"]([\w_.-]+)[\'"]$',
        read(INIT_PATH),
        re.M
    )

    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='subvenv',
    version=get_version(),
    description=(
        'A tool for creating virtualenv-friendly '
        'Sublime Text project files'
    ),
    long_description=get_readme_content(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    url='http://github.com/Railslide/subvenv',
    author='Giulia Vergottini',
    author_email='hello@railslide.io',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'click',
    ],
    test_suite='subvenv.tests',
    tests_require='nose',
    entry_points={
        'virtualenvwrapper.project.post_mkproject': [
            'subvenv = subvenv.core:post_mkproject',
        ],
        'console_scripts': [
            'subvenv = subvenv.core:cli'
        ],
    },
    include_package_data=True,
    zip_safe=False)
