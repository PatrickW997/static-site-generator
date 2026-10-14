import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        """
        This test wasn't part of the assignment, but was a first try to add a equality test
        """
        htmlnode = HTMLNode("h1", "This is a Test")
        expected_repr = 'tag: h1, \nvalue: This is a Test, \nchildren: None, \nprops: None'
        self.assertEqual(repr(htmlnode), expected_repr)

    def test_props_to_html(self):
        """
        Test for correct output after props formatting
        """
        node = HTMLNode("h1", "This is a Test", None, {"href": "https://www.google.com", "target": "_blank"})
        expected = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_none(self):
        """
        Test for empty sting if props are None
        """
        node = HTMLNode("h1", "This is a Test")
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        """
        Test for empty sting if props are an empty dictionary
        """
        node = HTMLNode("h1", "This is a Test", None, {})
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()

