#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

# Make PyPI play nice with markdown
# See xiongchiamiov's comment:
# https://coderwall.com/p/qawuyq/use-markdown-readme-s-in-python-modules
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = open('README.md').read()


setup(name='subvenv',
      version='1.0.1',
      description=('A tool for creating virtualenv-friendly '
                   'Sublime Text project files'),
      long_description=long_description,
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
      packages=find_packages(exclude=['*tests']),
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
