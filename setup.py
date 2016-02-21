#!/usr/bin/env python

from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='subvenv',
      version='1.0.0',
      description=('A tool for creating virtualenv-friendly '
                   'Sublime Text project files'),
      long_description=readme(),
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
      ],
      url='http://github.com/Railslide/subvenv',
      author='Giulia Vergottini',
      author_email='hello@railslide.io',
      license='MIT',
      packages=find_packages('subvenv', exclude=['tests']),
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
