# coding=utf-8

import os
import unittest

try:
    from mock import patch, mock_open
except ImportError:
    from unittest.mock import patch, mock_open


from subvenv import core


class SubvenvTests(unittest.TestCase):

    def shortDescription(self):
        """ Make nose display test names instead of docstrings. """
        return None

    @patch.object(core, 'create_sublime_project_file')
    @patch.object(os, 'getenv', return_value='test_env')
    def test_postmkproject_read_the_file(self, os_mock, create_sublime_mock):
        """
        Calling post_mkproject should result in the file located
        at env_name/.project to be read and its content to be
        passed to create_sublime_project_file.

        """
        m = mock_open(read_data='test_name')
        with patch('subvenv.core.open', m, create=True) as m:
            core.post_mkproject()

        m.assert_called_with('test_env/.project', 'r')
        create_sublime_mock.assert_called_with(
            'test_name',
            'test_env',
            'test_env/bin/python'
        )

    @patch.object(os, 'getenv', return_value='')
    def test_postmkproject_without_virtualenv(self, os_mock):
        """
        Running post_mkproject without being in a virtualenv
        should exit the program.

        """
        with self.assertRaises(SystemExit):
            core.post_mkproject()

    def test_create_sublime_project_file(self):
        """
        Calling create_sublime_project_file should write a
        file in the given projct folder.

        """
        m = mock_open()
        with patch('subvenv.core.open', m, create=True) as m:
            core.create_sublime_project_file(
                'test_folder',
                'test_name',
                'test_interpreter'
            )
        m.assert_called_with('test_folder/test_name.sublime-project', 'w')
        self.assertTrue(m.return_value.write.called)

    def test_create_sublime_project_file_with_non_existing_target_folder(self):
        """
        Trying to create a sublime project file into a non
        existing folder should exit the program.

        """
        with self.assertRaises(SystemExit):
            core.create_sublime_project_file(
                'nonexistingfolder',
                'test_name',
                'test_interpreter'
            )

    @patch.object(core, 'create_sublime_project_file')
    @patch.object(os, 'getenv', return_value="test_env")
    @patch.object(os, 'getcwd', return_value="")
    def test_make_project(self, getcwd_mock, getenv_mock, create_sublime_mock):
        """
        When executing succesfully make_project should
        call create_sublime_project_file.

        """
        core.make_project(folder='test_folder')
        create_sublime_mock.assert_called_with(
            'test_folder',
            'test_env',
            'test_env/bin/python'
        )

    @patch.object(os, 'getenv', return_value='')
    def test_make_project_without_virtualenv(self, os_mock):
        """
        Running make_project without being in a virtualenv
        should exit the program.

        """
        with self.assertRaises(SystemExit):
            core.make_project()

    @patch.object(os, 'getenv', return_value='')
    def test_get_virtualenv_without_virtualenv(self, os_mock):
        """
        Calling get_virtualenv without being in a virtualenv
        should raise an exception
        """
        with self.assertRaises(core.VirtualenvError):
            core.get_virtualenv()

    @patch.object(os, 'getenv', return_value='test/test_env')
    def test_get_virtualenv(self, os_mock):
        venv = core.get_virtualenv()

        self.assertEqual(venv.path, 'test/test_env')
        self.assertEqual(venv.interpreter, 'test/test_env/bin/python')
        self.assertEqual(venv.name, 'test_env')

    @patch.object(core, 'cli', return_value=('invalid_command', {}))
    def test_main_non_existing_command(self, cli_mock):
        """
        Calling main with a non existing command should exit
        the program
        """
        with self.assertRaises(SystemExit):
            core.main()

    @patch.object(core, 'cli', return_value=('make_project', {}))
    @patch.object(core, 'make_project')
    def test_main_make_project_with_no_folder(self, make_project_mock, cli_mock):
        """
        Calling main without specifying a target folder should
        result in make_project being called without any arguments
        """
        core.main()
        make_project_mock.assert_called_with()

    @patch.object(
        core,
        'cli',
        return_value=('make_project', {'folder': 'test_folder'})
    )
    @patch.object(core, 'make_project')
    def test_main_make_project_with_specified_folder(self, make_project_mock, cli_mock):
        """
        Calling main with a target folder specified should result in
        such a folder being passed down to make_project.
        """
        core.main()
        make_project_mock.assert_called_with(folder='test_folder')
