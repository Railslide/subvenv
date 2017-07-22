#!/usr/bin/env python
# coding=utf-8

import argparse
import json
import logging
import os
import sys

# import click

from collections import namedtuple

from subvenv.version import __version__


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


# @click.group(context_settings=HELP_COMMANDS)
# def cli():
#     """
#     Subvenv is a tool for creating virtualenv-friendly Sublime Text
#     project files.
#     It can be used  as a standalone or as a plugin for Virtualenwrapper.

#     See https://github.com/Railslide/subvenv for more information.
#     """
#     pass


# @cli.command()
# @click.option(
#     '--folder',
#     type=click.Path(),
#     help='Target folder for file creation.'
# )
def make_project(folder=None):
    """
    Create a Sublime project file for the current virtual environment.

    If no target folder is specified, the file will be created in
    the current working directory.

    """
    # import pdb; pdb.set_trace()
    if not folder:
        folder = os.getcwd()
    folder = os.path.abspath(folder)

    try:
        venv = get_virtualenv()
    except VirtualenvError:
        sys.exit('You need to be inside a virtualenv for using subvenv.')

    create_sublime_project_file(folder, venv.name, venv.interpreter)


def cli(args=None):
    parser = argparse.ArgumentParser(
        description=(
            'Subvenv is a tool for creating virtualenv-friendly Sublime Text '
            'project files.\n'

            'It can be used as a standalone or as a plugin for'
            ' Virtualenwrapper.\n\n'

            'See https://github.com/Railslide/subvenv for more information.'
        ),
        formatter_class=argparse.RawTextHelpFormatter,
        prog='subvenv'
    )

    # Version
    parser.add_argument(
        "-v", "--version",
        help="print version information and quit",
        action="version",
        version='%(prog)s ' + __version__
    )

    # Commands
    subparsers = parser.add_subparsers(dest='command', metavar='COMMAND')
    subparsers.required = True

    commands_make_project = subparsers.add_parser(
        'make_project',
        help='create a Sublime Text project file',
        description=(
            'Create a Sublime project file for the current virtual '
            'environment.\n\n'

            'If no target folder is specified, the file will be created in the'
            ' current\n'
            'working directory.'
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    commands_make_project.add_argument(
        '--folder',
        help='target folder for file creation (default: current directory)'
    )

    kwargs = vars(parser.parse_args(args))
    command = kwargs.pop('command')
    return command, kwargs


def main():
    command, kwargs = cli()

    FUNCTION_MAP = {
        'make_project': make_project
    }
    try:
        FUNCTION_MAP[command](**kwargs)
    except KeyError:
        sys.exit('Invalid command')


if __name__ == '__main__':
    main()
    # cli()
