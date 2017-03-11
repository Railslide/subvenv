#!/usr/bin/env python
# coding=utf-8

import json
import logging
import os
import sys

import click

from collections import namedtuple


log = logging.getLogger(__name__)


HELP_COMMANDS = dict(help_option_names=['-h', '--help'])


class VirtualenvError(Exception):
    pass


def get_virtualenv():
    path = os.getenv('VIRTUAL_ENV')

    if not path:
        raise VirtualenvError(
            'Trying to get virtualenv data while not in a virtualenv'
        )

    name = os.path.basename(path)
    interpreter = os.path.join(path, 'bin', 'python')

    Virtualenv = namedtuple('Virtualenv', ['name', 'path', 'interpreter'])
    return Virtualenv(name, path, interpreter)


def post_mkproject(args=None):
    """
    Create a Sublime text project file on virtualenvwrapper project
    creation.
    """
    try:
        venv = get_virtualenv()
    except VirtualenvError:
        sys.exit('You need to be inside a virtualenv for using subvenv.')

    project_path_file = os.path.join(venv.path, '.project')

    try:
        with open(project_path_file, 'r') as f:
            project_folder = f.readline().rstrip('\r\n')
    except IOError:
        sys.exit('Virtualenv project not found.\n')

    create_sublime_project_file(project_folder, venv.name, venv.interpreter)


def create_sublime_project_file(project_folder, project_name, interpreter):
    """
    Create a Sublime Text project file in the given project folder.

    Args:
        project_folder (str): path to project folder
        project_name (str): name of the project
        interpreter (str): path to the Python interpreter used for
                           the project

    """
    sublime_file_name = "{}.sublime-project".format(project_name)
    settings_text = {
        "folders": [
            {
                "follow_symlinks": True,
                "path": project_folder,
            },
        ],
        "settings": {
            "python_interpreter": interpreter,
        },
    }
    target_path = (os.path.join(project_folder, sublime_file_name))

    try:
        with open(target_path, 'w') as f:
            f.write(json.dumps(settings_text, sort_keys=True, indent=4))
    except IOError:
        sys.exit(
            'Cannot create file.\n\
             Attempted path: {}'.format(project_folder)
        )


@click.group(context_settings=HELP_COMMANDS)
def cli():
    """
    Subvenv is a tool for creating virtualenv-friendly Sublime Text
    project files.
    It can be used  as a standalone or as a plugin for Virtualenwrapper.

    See https://github.com/Railslide/subvenv for more information.
    """
    pass


@cli.command()
@click.option(
    '--folder',
    type=click.Path(),
    help='Target folder for file creation.'
)
def make_project(folder=None):
    """
    Create a Sublime project file for the current virtual environment.

    If no target folder is specified, the file will be created in
    the current working directory.

    """
    if not folder:
        folder = os.getcwd()

    folder = os.path.abspath(folder)

    try:
        venv = get_virtualenv()
    except VirtualenvError:
        sys.exit('You need to be inside a virtualenv for using subvenv.')

    create_sublime_project_file(folder, venv.name, venv.interpreter)


if __name__ == '__main__':
    cli()
