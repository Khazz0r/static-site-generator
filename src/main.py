import os, shutil
from textnode import TextNode

def main():
    copy_static_to_public("static/", "public/")


def copy_static_to_public(static_dir, public_dir):
    if not os.path.exists(static_dir):
        raise FileNotFoundError(f"Static directory '{static_dir}' does not exist.")
    
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)
    
    recursive_file_dir_copy(static_dir, public_dir)


def recursive_file_dir_copy(static_src, public_dest):
    for item in os.listdir(static_src):
        src_path = os.path.join(static_src, item)
        dest_path = os.path.join(public_dest, item)
        
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            os.mkdir(dest_path)
            recursive_file_dir_copy(src_path, dest_path)


main()