Subvenv
=======

Subvenv makes the creation of virtualenv-friendly Sublime Text 2/3 project files as easy as
`subvenv --make-project`[?].

Create your virtualenv, run subvenv, and you're ready to code.


TOC
---
* [Installation](#installation)
* [License](#license)

Installation
------------

Clone the repo

    git clone https://github.com/Railslide/subvenv.git

and from the `subvenv` folder give

    python setup.py install


Supported virtualenv managers
-----------------------------

Subvenv supports Virtualenv, Virtualenwrapper, and pyvenv.

Any other virtualenv manager making use of the `VIRTUALENV` environment variable should probably work too.


Virtualenvwrapper projects integration
--------------------------------------

Using Virtualenvwrapper projects removes the need of manually running Subvenv. Project creation will activate Subvenv behind the scenes and a Sublime project file will be automagically created inside the project folder.


License
-------

MIT license. See `LICENSE` file for more information.
