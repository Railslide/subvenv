Subvenv
=======

Subvenv makes the creation of virtualenv-friendly Sublime Text 2/3 project files as easy as
`subvenv make_project` (or even skipping it by integrating it with Virtualenwrapper!).

Create your virtualenv, run subvenv, and you're ready to code.

Bonus point: besides saving you the time of manually creating a project files, it also makes linting plugins like [Anaconda](https://github.com/DamnWidget/anaconda) and [SublimePythonIDE](https://github.com/JulianEberius/SublimePythonIDE) work out of the box!

Table of contents
-----------------

* [Installation](#installation)
* [Virtualenvwrapper projects integration](#virtualenvwrapper-projects-integration)
* [Usage as a standalone](#usage-as-a-standalone)
* [Supported Python versions](#supported-python-versions)
* [Supported virtualenv managers](#supported-virtualenv-managers)
* [Contributions](#contributions)
* [License](#License)


Installation
------------

You can install the latest stable release via pip:

    $ pip install subvenv


Virtualenvwrapper projects integration
--------------------------------------

Using [Virtualenvwrapper projects](http://virtualenvwrapper.readthedocs.org/en/latest/projects.html#project-management) removes the need of manually running Subvenv. Project creation will activate Subvenv behind the scenes and a Sublime project file will be automagically created inside the project folder.

Simply create a new virtualenv with

     $ mkproject <project_name>

and a `<project_name>.sublime-project` file will be placed in your `/your/project/home/<project_name>/`. Open it with Sublime Text and you are ready to go.


Usage as a standalone
----------------------

If you don't want to pass through a Virtualenwrapper project

    $ subvenv make_project

will create a `<virtualenv_name>.sublime-project` file in the current working directory.


You can also specify a location different than the current folder by using the `--folder` flag

    $ subvenv make_project --folder=path/to/target_folder


Supported Python versions
-------------------------

Subvenv is tested under Python 2.7, 3.3, 3.4, 3.5, 3.6.


Supported virtualenv managers
-----------------------------

Subvenv supports Virtualenv, Virtualenwrapper, and pyvenv.

Any other virtualenv manager making use of the `VIRTUALENV` environment variable should probably work too.



Contributions
-------------

Are highly appreciated :)

Just follow PEP8 if you're going to submit code.

License
-------

MIT license. See `LICENSE` file for more information.
