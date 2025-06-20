# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


# class TestGetFilesInfo(unittest.TestCase):
# 
#     def test_error_bin(self):
#         result = get_files_info("calculator", "/bin")
#         print(result)
#         self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')
# 
#     def test_error_double_dot(self):
#         result = get_files_info("calculator", "pkg/../../")
#         print(result)
#         self.assertEqual(result, 'Error: Cannot list "pkg/../../" as it is outside the permitted working directory')
# 
#     def test_error_not_a_dir(self):
#         result = get_files_info("calculator", "tests.py")
#         print(result)
#         self.assertEqual(result, 'Error: "tests.py" is not a directory.')
# 
#     def test_success_list_dir(self):
#         result = get_files_info("calculator", ".")
#         print(result)
#         expected = "tests.py: file_size: 1343 bytes, is_dir=False\nmain.py: file_size: 576 bytes, is_dir=False\npkg: file_size: 128 bytes, is_dir=True\n"
#         self.assertEqual(result, expected)
# 
#     def test_success_list_dir_2(self):
#         result = get_files_info("calculator", "pkg")
#         print(result)
#         expected = "render.py: file_size: 767 bytes, is_dir=False\ncalculator.py: file_size: 1738 bytes, is_dir=False\n"
#         self.assertEqual(result, expected)
# 
# 
# class TestGetFileContent(unittest.TestCase):
# 
#     def test_main(self):
#         result = get_file_content("calculator", "main.py")
#         print(result)
# 
#     def test_calculator(self):
#         result = get_file_content("calculator", "pkg/calculator.py")
#         print(result)
# 
#     def test_bin_cat(self):
#         result = get_file_content("calculator", "/bin/cat")
#         print(result)


# class TestWriteFile(unittest.TestCase):
# 
#     def test_main(self):
#         print(write_file('calculator', 'lorem.txt', "wait, this isn't lorem ipsum"))
#         print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
#         print(write_file('calculator', '/tmp/temp.txt', "this should not be allowed"))


class TestExecuteFile(unittest.TestCase):

    def test_main(self):
        print(run_python_file('calculator', 'main.py'))
        print(run_python_file('calculator', 'tests.py'))
        print(run_python_file('calculator', '../main.py'))
        print(run_python_file('calculator', 'nonexistent.py'))


if __name__ == "__main__":
    unittest.main()
