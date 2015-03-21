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
    project_interpreter = os.path.join(project_venv, 'bin/python')

    try:
        with open(project_path_file, 'r') as f:
            project_folder = f.readline().rstrip('\r\n')
    except IOError:
        sys.stderr.write('Virtualenv project not found.\n')
        return

    create_sublime_project(project_folder, project_name, project_interpreter)


def create_sublime_project(project_folder, project_name, interpreter, *args):
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

    with open(target_path, 'w') as f:
        f.write(json.dumps(settings_text, sort_keys=True, indent=4))

    return
