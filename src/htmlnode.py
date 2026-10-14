

class HTMLNode:
    """
    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    children - A list of HTMLNode objects representing the children of this node
    props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """
    def __init__(self,
                 tag: str | None = None,
                 value: str | None = None,
                 children: list | None = None,
                 props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"tag: {self.tag}, \nvalue: {self.value}, \nchildren: {self.children}, \nprops: {self.props}"

    def to_html(self):
        raise Exception(NotImplementedError)

    def props_to_html(self):
        if not self.props: # It’s true for both None and an empty dictionary. | alernative >> if self.props == None or self.props == {}:
            return ""

        formatted_string = ""
        for key in self.props:
            formatted_string += f" {key}=\"{self.props[key]}\""
        return formatted_string
