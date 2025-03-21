import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter == "**" or delimiter == "_" or delimiter == "`":
        new_nodes = []

        for node in old_nodes:
            if node.text_type != TextType.NORMAL:
                new_nodes.append(node)
                continue
            split_text = node.text.split(delimiter)
            for i in range(len(split_text)):
                if split_text[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_text[i], TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(split_text[i], text_type))
                        
        return new_nodes
    
    else:
        raise Exception("delimiter selected is not a valid delimiter")

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
