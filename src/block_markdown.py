import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered.append(block)
    return filtered

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return "heading"
    if block.startswith("```") and block.endswith("```"):
        return "code"
    
    lines = block.split('\n')
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                break
        else:
            return "quote"
            
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                break
        else:
            return "unordered_list"
            
    if block.startswith("1. "):
        current_num = 1
        for line in lines:
            if not line.startswith(f"{current_num}. "):
                break
            current_num += 1
        else:
            return "ordered_list"
            
    return "paragraph"