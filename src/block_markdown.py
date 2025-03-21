from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    while "" in blocks:
        blocks.remove("")

    for block in blocks:
        block = block.strip()
        filtered_blocks.append(block)
        
    return filtered_blocks
