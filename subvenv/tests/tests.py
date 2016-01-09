import os
import sys
import unittest
from unittest.mock import patch, mock_open

from click.testing import CliRunner

from subvenv import core


class SubvenvTests(unittest.TestCase):

    def shortDescription(self):
        """ Make nose display test names instead of docstring. """
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
        with patch('builtins.open', m, create=True) as m:
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
        with patch('builtins.open', m, create=True) as m:
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
    def test_make_project(self, os_mock, create_sublime_mock):
        """
        When executing succesfully make_project should
        call create_sublime_project_file.

        """
        runner = CliRunner()
        runner.invoke(core.make_project, ['--folder', 'test_folder'])
        create_sublime_mock.assert_called_with(
            'test_folder',
            'test_env',
            sys.executable
        )

    @patch.object(os, 'getenv', return_value='')
    def test_make_project_without_virtualenv(self, os_mock):
        """
        Running make_project without being in a virtualenv
        should exit the program.

        """
        runner = CliRunner()
        result = runner.invoke(core.make_project)
        expected_msg = 'You need to be inside a virtualenv for using subvenv.'

        self.assertTrue(isinstance(result.exception, SystemExit))
        self.assertEqual(result.exception.args[0], expected_msg)
