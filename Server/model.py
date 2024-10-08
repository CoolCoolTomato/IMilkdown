from Server.sdk.sdk import *

class Node:
    def __init__(self, path="", name="", is_folder=False):
        self.path = path
        self.name = name
        self.is_folder = is_folder
        self.sub_nodes = []

    def add_sub_node(self, sub_node):
        self.sub_nodes.append(sub_node)
        folders = [x for x in self.sub_nodes if x.is_folder]
        folders.sort(key=lambda x : x.name)
        files = [x for x in self.sub_nodes if not x.is_folder]
        files.sort(key=lambda x : x.name)
        self.sub_nodes = folders + files


    def remove_sub_node(self, path):
        self.sub_nodes = [x for x in self.sub_nodes if x.path != path]

    def build_node(self):
        if self.is_folder:
            folders = get_folders(self.path)
            for folder in folders:
                node = Node(path=folder, name=folder.split("/")[-1], is_folder=True)
                node.build_node()
                self.add_sub_node(node)

            files = get_files(self.path)
            for file in files:
                node = Node(path=file, name=file.split("/")[-1], is_folder=False)
                self.add_sub_node(node)
