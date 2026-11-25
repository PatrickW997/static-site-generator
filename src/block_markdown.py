from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list:
    split_markdown: list = markdown.split("\n\n")
    clean_list: list = []
    for element in split_markdown:
        if element.strip() != "":
            clean_list.append(element.strip())
    return clean_list


def block_to_block_type(md_text_block: str) -> BlockType:
    # check for HEADING
    if re.match("(#){1,6} .+", md_text_block):
        return BlockType.HEADING

    # check for CODE
    if md_text_block.startswith("```\n") and md_text_block.endswith("```"):
        return BlockType.CODE

    # check for QUOTE
    if all(map(lambda x : x.startswith(">"), md_text_block.split("\n"))):
        return BlockType.QUOTE
    # -alternative-
    #    md_text_block_lines = md_text_block.split("\n")
    #    is_quote = True
    #    for line in md_text_block_lines:
    #        if not line.startswith(">"):
    #            is_quote = False
    #            break
    #    if is_quote:
    #    return BlockType.QUOTE

    # check for UNORDERED_LIST
    if all(map(lambda x : x.startswith("- "), md_text_block.split("\n"))):
        return BlockType.UNORDERED_LIST

    # check for ORDERED_LIST
    if all(map(lambda x, y : x.startswith(f"{y}. "), md_text_block.split("\n"), range(1,len(md_text_block.splitlines())+1))):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str) -> ParentNode:
    md_block_list = markdown_to_blocks(markdown)
    converted_markdown = []
    for block in md_block_list:
        block_blocktype = block_to_block_type(block)
        if block_blocktype == BlockType.PARAGRAPH:
            converted_markdown.append(ParentNode("p", [])) # children has to be filled in instead of empty list
    return ParentNode("div",converted_markdown)

def text_to_children(text_value : str) -> list[HTMLNode]: # helper function that will find children for above
    pass