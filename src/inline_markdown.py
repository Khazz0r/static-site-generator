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
    

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def text_to_textnodes(text):
    all_nodes = [TextNode(text, TextType.NORMAL)]
    all_nodes = split_nodes_delimiter(all_nodes, "**", TextType.BOLD)
    all_nodes = split_nodes_delimiter(all_nodes, "_", TextType.ITALIC)
    all_nodes = split_nodes_delimiter(all_nodes, "`", TextType.CODE)
    all_nodes = split_nodes_image(all_nodes)
    all_nodes = split_nodes_link(all_nodes)
    return all_nodes
