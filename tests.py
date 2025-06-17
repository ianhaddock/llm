# tests.py

import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):

    def test_simple(self):
        result = get_files_info("calculator", ".")
        self.assertEqual(result, "main.py: file_size: 576 bytes, is_dir=False")


if __name__ == "__main__":
    unittest.main()
