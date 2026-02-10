import unittest
from copystatic import *

class TestCopyStatic(unittest.Testcase):
    def test_basic_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_h1_with_whitespace(self):
        self.assertEqual(extract_title("#   Space Case   "), "Space Case")

    def test_multiline_markdown(self):
        md = "Some text\n# Actual Title\nMore text"
        self.assertEqual(extract_title(md), "Actual Title")

    def test_no_h1_raises_error(self):
        with self.assertRaises(Exception):
            extract_title("## Only an H2")

    def test_empty_string_raises_error(self):
        with self.assertRaises(Exception):
            extract_title("")

if __name__ == "__main__":
    unittest.main()