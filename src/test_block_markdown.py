# test_block_markdown.py
import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

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
        blocks_2 = markdown_to_blocks("    ")
        self.assertEqual(blocks, [])
        self.assertEqual(blocks_2, [])


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_and_code(self):
        self.assertEqual(block_to_block_type("# heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### heading 6"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)

    def test_quote_and_lists(self):
        self.assertEqual(block_to_block_type("> a\n> b"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- a\n- b"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. a\n2. b\n3. c"), BlockType.ORDERED_LIST)

    def test_paragraph_fallbacks(self):
        self.assertEqual(block_to_block_type("just text\nmore text"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("####### seven"), BlockType.PARAGRAPH) # shouldn't match heading as max "#" are supported
        self.assertEqual(block_to_block_type("- a\nb"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("2. a\n3. b"), BlockType.PARAGRAPH)
