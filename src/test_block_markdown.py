# test_block_markdown.py
import unittest
from block_markdown import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
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


    def test_markdown_to_blocks_excessive_newlines(self):
        md = """
First block



Second block with trailing spaces




Third block
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First block",
                "Second block with trailing spaces",
                "Third block",
            ],
        )



    def test_markdown_to_blocks_empty(self):
        blocks = markdown_to_blocks("")
        blocks_2 = markdown_to_blocks("")
        self.assertEqual(blocks, [])
        self.assertEqual(blocks_2, [])
