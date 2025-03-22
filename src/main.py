import os, shutil, sys
from block_markdown import markdown_to_html_node

def main():
    basepath = sys.argv[1]
    if basepath == "":
        basepath = "/"
        
    copy_static_to_public("static/", "docs/")
    generate_pages_recursive(basepath, "content/", "template.html", "docs/")


def copy_static_to_public(static_dir, public_dir):
    if not os.path.exists(static_dir):
        raise FileNotFoundError(f"Static directory '{static_dir}' does not exist.")
    
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)
    
    recursive_file_dir_copy(static_dir, public_dir)


def recursive_file_dir_copy(static_src, public_dest):
    for file in os.listdir(static_src):
        src_path = os.path.join(static_src, file)
        dest_path = os.path.join(public_dest, file)
        
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            os.mkdir(dest_path)
            recursive_file_dir_copy(src_path, dest_path)


def extract_title(markdown):
    file_text_lines = markdown.split("\n")
    if file_text_lines[0].startswith("#"):
        h1_header = file_text_lines[0].strip("#").strip()
        return h1_header
    else:
        raise Exception("header not found")


def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path, "r") as file:
        markdown_contents = file.read()
    
    with open(template_path, "r") as file:
        template_contents = file.read()
    
    html_contents = markdown_to_html_node(markdown_contents).to_html()
    title = extract_title(markdown_contents)

    replaced_template_contents = (template_contents.replace("{{ Title }}", title)
                                  .replace("{{ Content }}", html_contents)
                                  .replace('href="/', f'href="{basepath}')
                                  .replace('src="/', f'src="{basepath}')
                                  )

    dest_path = os.path.splitext(dest_path)[0] + ".html"

    with open(dest_path, "w") as file:
        file.write(replaced_template_contents)


def generate_pages_recursive(basepath, content_path, template_path, public_path):
    for file in os.listdir(content_path):
        src_path = os.path.join(content_path, file)
        dest_path = os.path.join(public_path, file)
    
        if os.path.isfile(src_path):
            generate_page(basepath, src_path, template_path, dest_path)
        else:
            os.mkdir(dest_path)
            generate_pages_recursive(basepath, src_path, template_path, dest_path)


main()
