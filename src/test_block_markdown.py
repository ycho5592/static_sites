import unittest
from block_markdown import *

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_headings(self):
        self.assertEqual(block_to_block_type("# Heading"), "heading")
        self.assertEqual(block_to_block_type("###### Small Heading"), "heading")
        self.assertEqual(block_to_block_type("####### Too many hashes"), "paragraph")
        self.assertEqual(block_to_block_type("#NoSpace"), "paragraph")

    def test_code_blocks(self):
        code_block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(code_block), "code")
        self.assertEqual(block_to_block_type("```no closing"), "paragraph")

    def test_quote_blocks(self):
        self.assertEqual(block_to_block_type("> This is a quote"), "quote")
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2"), "quote")
        self.assertEqual(block_to_block_type("> Line 1\nLine 2"), "paragraph")

    def test_unordered_lists(self):
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("- Item 1\n* Item 2"), "paragraph")
        self.assertEqual(block_to_block_type("-No space"), "paragraph")

    def test_ordered_lists(self):
        self.assertEqual(block_to_block_type("1. First\n2. Second\n3. Third"), "ordered_list")
        # Test wrong starting number
        self.assertEqual(block_to_block_type("2. Start at two"), "paragraph")
        # Test broken increment
        self.assertEqual(block_to_block_type("1. First\n3. Third"), "paragraph")
        # Test missing space
        self.assertEqual(block_to_block_type("1.First"), "paragraph")

    def test_paragraphs(self):
        self.assertEqual(block_to_block_type("Just a normal paragraph."), "paragraph")
        self.assertEqual(block_to_block_type("  "), "paragraph")

if __name__ == "__main__":
    unittest.main()