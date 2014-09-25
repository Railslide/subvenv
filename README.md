Subvenv (WIP)
=============

Subvenv is a plugin for Dough Hellman's Virtualenvwrapper that extends the `mkproject` functionality. When a new Virtualenvwrapper project is created Subvenv automagically places a Sublime Text 2/3 settings file in the project folder.

Here is how the Subven sublime-project settings file looks like:

    {
        "folders":
        [
            {
                "follow_symlinks": true,
                "path": "path/to/project/folder"
            }
        ],
        "settings":
        {
            "python_interpreter": "/path/to/virtualenv/bin/python",
        },
    }
    

License
-------

MIT license. See `LICENSE` file for more information.


