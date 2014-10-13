Subvenv
=======

Subvenv is a [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) plugin that automatically generates Sublime Text 2/3 project files.

* It saves you the time to manually create a project files
* It makes linting plugins like [Anaconda](https://github.com/DamnWidget/anaconda) and [SublimePythonIDE](https://github.com/JulianEberius/SublimePythonIDE) working out of the box, without the need of further settings.

Requirements
------------

Projects must be enabled in Virtualenvwrapper in order to use Subvenv.

For enabling Virtualenvwrapper, make sure the following line is present in your shell startup file (`.bashrc`, `.profile`, etc.):

    export PROJECT_HOME=/path/to/your/projects/folder/

**IMPORTANT**: when adding it manually make sure to place it before the line sourcing virtualenwrapper.sh (`source /usr/local/bin/virtualenvwrapper.sh`)

Installation
------------

Clone the repo

    git clone https://github.com/Railslide/subvenv.git

and from the `subvenv` folder give

    python setup.py install


Usage
-----

Create a new virtualenv with `mkproject <project_name>`. From Sublime Text open the project `<project_name>.sublime-project` located in your `/your/project/home/<project_name>/` and you are ready to go.

What's in the generated file
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

Contribution guidelines
-----------------------

Check open issues first, if nobody has reported your problem yet open a new one.

You know how to fix a bug? Awesome! Fork the repository, make your changes in a new branch, and send a pull request.

Do you have a killer idea for improving Subenv? I'd love to hear about it! Just create a new issue, so we can discuss about it.

License
-------

MIT license. See `LICENSE` file for more information.


