#!/usr/bin/env python

import json
import logging
import os
import sys


log = logging.getLogger(__name__)


def post_mkproject(args=None):
    project_venv = os.getenv('VIRTUAL_ENV')
    project_name = os.path.basename(project_venv)
    project_path_file = os.path.join(project_venv, '.project')
    interpreter = os.path.join(project_venv, 'bin/python')

    try:
        with open(project_path_file, 'r') as f:
            project_folder = f.readline().rstrip('\r\n')
    except IOError:
        sys.exit('Virtualenv project not found.\n')

    create_sublime_project_file(project_folder, project_name, interpreter)


def make_project(target_folder=None):
    if not target_folder:
        target_folder = os.getcwd()

    venv_path = os.getenv('VIRTUAL_ENV')

    if not venv_path:
        sys.exit('You need to be inside a virtualenv for using subvenv.')

    project_name = os.path.basename(venv_path)
    interpreter = sys.executable

    create_sublime_project_file(target_folder, project_name, interpreter)


def create_sublime_project_file(project_folder, project_name, interpreter):
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
