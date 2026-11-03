import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImage(unittest.TestCase):
    """
    Test the image extraction from extract_markdown_images function is working correct
    """
    def test_extract_markdown_images_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertListEqual(expected, extract_markdown_images(text))

    def test_extract_markdown_images_2(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]

        self.assertListEqual(expected,  extract_markdown_images(text))

class TestExtractMarkdownURL(unittest.TestCase):
    """
    Test the url extraction from extract_markdown_images function is working correct
    """
    def test_extract_markdown_links_1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(expected, extract_markdown_links(text))



# to make the test execute when running the file itself
# python src/test_extract_markdown.py
if __name__ == "__main__":
    unittest.main()
