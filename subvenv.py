import json
import logging
import os


log = logging.getLogger(__name__)


def post_mkproject(args):
    project_name = args
    project_venv = os.path.join(os.getenv('WORKON_HOME'), project_name)
    project_path_file = os.path.join(project_venv, '.project')
    project_interpreter = os.path.join(project_venv, 'bin/python')

    with open(project_path_file, 'r') as pf:
        project_folder = pf.readline()

    sublime_project_file = "{}.sublime-project".format(project_name)
    settings_text = {
        "folders": {
            "path": project_folder,
        },
        "settings": {
            "python_interpreter": project_interpreter,
        },
    }
    json.dumps(settings_text, indent=4)

    print(project_name)
    print(project_interpreter, project_folder, sublime_project_file)


if __name__ == '__main__':
    post_mkproject('fyndiq')
