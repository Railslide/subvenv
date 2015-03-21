from setuptools import setup, find_packages

setup(name='subvenv',
      version='0.1',
      description=('A Virtualenvwrapper plugin that automatically '
                   'generates Sublime Text 2/3 project files'),
      url='http://github.com/Railslide/subvenv',
      author='Giulia Vergottini',
      author_email='hello@railslide.io',
      license='MIT',
      namespace_packages=['virtualenvwrapper'],
      packages=find_packages(),

      entry_points={
          'virtualenvwrapper.project.post_mkproject': [
              'subvenv = virtualenvwrapper.subvenv:post_mkproject',
          ],
          'console_scripts': [
            'subvenv = virtualenvwrapper.subvenv:post_mkproject'
          ],
      },

      zip_safe=False)
