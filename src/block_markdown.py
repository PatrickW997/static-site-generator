from textnode import TextNode, TextType
import re

def markdown_to_blocks(markdown: str) -> list:
    split_markdown: list = markdown.split("\n\n")
    clean_list: list = []
    for element in split_markdown:
        if element.strip() != "":
            clean_list.append(element.strip())
    return clean_list
