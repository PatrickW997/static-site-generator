from textnode import TextNode, TextType
import re

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


def extract_markdown_images(text) -> list[tuple]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text) -> list[tuple]:
    return re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue  # (or use elif)
        left_text_in_node = node.text
        images = extract_markdown_images(node.text)
        for image in images:
            md_string = f"![{image[0]}]({image[1]})"
            sections = left_text_in_node.split(md_string, 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))
            left_text_in_node = sections[1]
        if left_text_in_node:
            new_nodes.append(TextNode(left_text_in_node,TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue  # (or use elif)
        left_text_in_node = node.text
        links = extract_markdown_links(node.text)
        for link in links:
            md_string = f"[{link[0]}]({link[1]})"
            sections = left_text_in_node.split(md_string, 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0],TextType.LINK,link[1]))
            left_text_in_node = sections[1]
        if left_text_in_node:
            new_nodes.append(TextNode(left_text_in_node,TextType.TEXT))
    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    # alternative with nested calls
    # nodes = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(nodes, "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
