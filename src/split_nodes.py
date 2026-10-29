from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif delimiter not in node.text:
            new_nodes.append(node)
        elif not node.text.count(delimiter) % 2 == 0:
            raise Exception(f"Uneven delimiter count for '{delimiter}'")
        else:
            split_text = node.text.split(delimiter)
            for index in range(len(split_text)):
                if split_text[index] == "":
                    continue
                elif index % 2 != 0:
                    new_nodes.append(TextNode(split_text[index], text_type))
                else:
                    new_nodes.append(TextNode(split_text[index], TextType.TEXT))
    return new_nodes
