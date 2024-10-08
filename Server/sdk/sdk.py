import os
import shutil

def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

def get_files(path):
    return [os.path.abspath(os.path.join(path, f)) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def get_folders(path):
    return [os.path.abspath(os.path.join(path, f)) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

def create_file(path):
    with open(path, 'w', encoding='utf-8') as file:
        pass

def create_folder(path):
    os.makedirs(path, exist_ok=True)

def rename_file(old_path, new_path):
    os.rename(old_path, new_path)

def rename_folder(old_path, new_path):
    os.rename(old_path, new_path)

def delete_file(path):
    os.remove(path)

def delete_folder(path):
    shutil.rmtree(path)