import os
import unittest

from unittest.mock import patch

from subvenv import subvenv


class SubvenvTests(unittest.TestCase):

    # @patch.object(os, 'getenv', return_value='test_env')
    # def test_postmkproject(self):
    #     pass

    @patch.object(os, 'getenv', return_value='')
    def test_postmkproject_without_env(self, os_mock):
        """
        Running post_mkproject without being in an env
        should exit the program.
        """
        with self.assertRaises(SystemExit):
            subvenv.post_mkproject()
