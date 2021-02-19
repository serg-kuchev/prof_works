from app import *
from unittest.mock import patch
import unittest


class test_some_function(unittest.TestCase):

    # @patch('builtins.input', lambda *args: 'y')
    def test_owner_name(self):
        self.assertEqual('Василий Гупкин', get_doc_owner_name('2207 876234'))

    def test_delete(self):
        self.assertTrue(delete_doc('11-2'))

    def test_add(self):
        self.assertTrue(add_new_doc('1', 'pr', 'Man', '4'))


if __name__ == '__main__':
    unittest.main()
