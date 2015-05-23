import os
import sys
import unittest

from unittest.mock import patch

from subvenv import subvenv


class SubvenvTests(unittest.TestCase):

    # @patch.object(os, 'getenv', return_value='test_env')
    # def test_postmkproject(self):
    #     pass

    @patch.object(os, 'getenv', return_value='')
    def test_postmkproject_without_virtualenv(self, os_mock):
        """
        Running post_mkproject without being in a virtualenv
        should exit the program.
        """
        with self.assertRaises(SystemExit):
            subvenv.post_mkproject()

    def test_create_sublime_project_file_with_non_existing_target_folder(self):
        """
        Trying to create a sublime project file into a non
        existing folder should exit the program.
        """
        with self.assertRaises(SystemExit):
            subvenv.create_sublime_project_file(
                'nonexistingfolder',
                'test_name',
                'test_interpreter'
            )

    @patch.object(subvenv, 'create_sublime_project_file')
    @patch.object(os, 'getenv', return_value="test_env")
    def test_make_project(self, os_mock, create_sublime_mock):
        """
        When executing succesfully make_mkproject should
        call create_sublime_project_file.
        """
        subvenv.make_project('test_folder')
        create_sublime_mock.assert_called_with(
            'test_folder',
            'test_env',
            sys.executable
        )

    @patch.object(os, 'getenv', return_value='')
    def test_make_project_without_virtualenv(self, os_mock):
        """
        Running make_mkproject without being in a virtualenv
        should exit the program.
        """
        with self.assertRaises(SystemExit):
            subvenv.make_project()
