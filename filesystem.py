class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        FileSystem._validate_path(path)

        path_node_names = path[1:].split("/")
        middle_node_names = path[:-1]
        new_directory_name = path[-1]

        before_last_node = self._find_bottom_node(middle_node_names)

        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node.name} is not a directory and therefore cannot have other nodes within it.")

        new_directory = Directory(new_directory_name)
        before_last_node.add_node(new_directory)

    def create_file(self, path, contents):
        FileSystem._validate_path(path)

        path_node_names = path[1:].split("/")
        middle_node_names = path[:-1]
        new_file_name = path[-1]

        before_last_node = self._find_bottom_node(middle_node_names)

        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node.name} is not a directory and therefore cannot have other nodes within it.")

        new_file = File(new_file_name) 
        new_file.write_contents(contents)

        before_last_node.add_node(new_file_name)

    def read_file(self, path):
        FileSystem._validate_path(path)

        path_node_names = path[1:].split("/")
        middle_node_names = path[:-1]
        file_name = path[-1]

        before_last_node = self._find_bottom_node(middle_node_names)

        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node.name} is not a directory and therefore cannot have other nodes within it.")
        
        if file_name not in before_last_node.children:
            raise ValueError(f"{file_name} does not exist.")
        
        return before_last_node.children[file_name].contents


    def delete_directory_or_file(self, path):
        FileSystem._validate_path(path)

        path_node_names = path[1:].split("/")
        middle_node_names = path[:-1]
        delete_this_item = path[-1]

        before_last_node = self._find_bottom_node(middle_node_names)

        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node.name} is not a directory and therefore cannot have other nodes within it.")
        
        if delete_this_item not in before_last_node.children:
            raise ValueError(f"{delete_this_item} is not in {before_last_node.name}.")
        
        before_last_node.delete_node(delete_this_item)

    def size(self):
        size = 0
        nodes = [self.root]
        while nodes > 0:
            current_node = nodes.pop()
            if isinstance(current_node, Directory):
                children = list(current_node.children.values())
                nodes.extend(children)
                continue
            
            if isinstance(current_node, File):
                size += len(current_node)
            
            return size

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")


    def _find_bottom_node(self, node_names):
        current_node = self.root

        for node_name in node_names:
            if not isinstance(node_name, Directory):
                raise ValueError(f"{node_name} is not a directory and therefore cannot have other nodes within it.")
            
            if node_name not in current_node.children:
                raise ValueError(f"Node not found: {node_name}")
            
            current_node = current_node.children[node_name]

        return current_node


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)
