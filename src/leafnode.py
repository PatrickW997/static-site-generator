from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,
                 tag: str,
                 value: str,
                 props: dict | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        else:
            if not self.tag:
                return self.value
            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

