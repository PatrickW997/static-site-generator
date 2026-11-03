import unittest
from extract_markdown import extract_markdown_images

class TestExtractMarkdownImage(unittest.TestCase):
    def test_image_extraction(self):
        """
        Test the image extraction from extract_markdown_images function is working correct
        """
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertListEqual(expected, extract_markdown_images(text))