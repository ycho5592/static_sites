import os
import shutil

from copystatic import copy_files_recursive

source_path = "./static"
dest_path = "./public"

def main():
    
    print("Cleaning public directory...")
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    
    print("Copying static files to public...")
    copy_files_recursive(source_path, dest_path)

if __name__ == "__main__":
    main()

