Subvenv (WIP)
=============

Subvenv is a [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) plugin that automatically generates Sublime Text 2/3 project files.

* It saves you the time to manually create a project files
* It makes linting plugins like Anaconda and SublimePythonIDE working out of the box, without the need of further settings.

Requirements
------------

Projects must be enabled in Virtualenvwrapper in order to use Subvenv.

For enabling Virtualenvwrapper, make sure the following line is present in your shell startup file (`.bashrc`, `.profile`, etc.):

    export PROJECT_HOME=/path/to/your/projects/folder/

**IMPORTANT**: when adding it manually make sure to place it before the line sourcing virtualenwrapper.sh (`source /usr/local/bin/virtualenvwrapper.sh`)

Installation
------------

**IMPORTANT**: Subvenv is currently work in progress, so this instructions refers to the dev version.

Clone the repo

    git clone https://github.com/Railslide/subvenv.git

and from the `subvenv` folder give

    python setup.py install


Usage
-----

Create a new virtualenv with `mkproject <project_name>`. From Sublime Text open the project `<project_name>.sublime-project` located in your `/your/project/home/<project_name>/` and you are ready to go.

What's in the file
------------------

Here is how the Subvenv sublime-project settings file looks like:

    {
        "folders": [
            {
                "follow_symlinks": true,
                "path": "path/to/project/folder"
            }
        ],
        "settings": {
            "python_interpreter": "/path/to/virtualenv/bin/python",
        }
    }


License
-------

MIT license. See `LICENSE` file for more information.


