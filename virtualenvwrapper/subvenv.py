import json
import logging
import os


log = logging.getLogger(__name__)


def post_mkproject(args):
    project_name = os.path.split(os.getenv('PWD'))[1]
    project_venv = os.path.join(os.getenv('WORKON_HOME'), project_name)
    project_path_file = os.path.join(project_venv, '.project')
    project_interpreter = os.path.join(project_venv, 'bin/python')

    with open(project_path_file, 'r') as f:
        project_folder = f.readline().rstrip('\r\n')

    sublime_file_name = "{}.sublime-project".format(project_name)
    settings_text = {

        "folders":
        [
            {
                "follow_symlinks": True,
                "path": project_folder,
            },
        ],
        "settings":
        {
            "python_interpreter": project_interpreter,
        },
    }
    target_path = (os.path.join(project_folder, sublime_file_name))

    with open(target_path, 'w') as f:
        f.write(json.dumps(settings_text, sort_keys=True, indent=4))

    return


if __name__ == '__main__':
    post_mkproject('hello')
