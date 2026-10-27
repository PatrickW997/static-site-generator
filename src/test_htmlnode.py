import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):
    def test_leafnode_to_html(self):
        """
        Test for LeafNode creation behaviour
        """
        leafnode = LeafNode("h1", "This is a Test-LeafNode",{"href": "https://www.google.com", "target": "_blank"})
        expected = "<h1 href=\"https://www.google.com\" target=\"_blank\">This is a Test-LeafNode</h1>"
        self.assertEqual(leafnode.to_html(), expected)

    def test_leafnode_to_html_tag_none(self):
        """
        Test for LeafNode creation with tag=None
        """
        leafnode = LeafNode(None, "This is a Test-LeafNode",{"href": "https://www.google.com", "target": "_blank"})
        expected = "This is a Test-LeafNode"
        self.assertEqual(leafnode.to_html(), expected)

    def test_leafnode_to_html_value_none(self):
        """
        Test for LeafNode creation with value=None
        """
        leafnode = LeafNode("h1", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertRaises(ValueError, leafnode.to_html)


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )




if __name__ == "__main__":
    unittest.main()

