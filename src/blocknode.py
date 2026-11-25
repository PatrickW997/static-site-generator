from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

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
