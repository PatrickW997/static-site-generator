from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag is None:
            raise ValueError(f"No valid tag {self.tag}")
        if self.children is None:
            raise ValueError(f"No valid chlidren list {self.children}")
        to_html_string = ""
        for child in self.children:
            to_html_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{to_html_string}</{self.tag}>"
