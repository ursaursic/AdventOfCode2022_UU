from __future__ import annotations


INPUT = "puzzleInputs/day7.txt"


class TreeNode:
    def __init__(self, dir_name) -> None:
        self.dir_name = dir_name
        self.children = []
        self.parent = None
        self.files = []
        self.total_size = 0
    
    def __lt__(self, other: TreeNode) -> bool:
         return self.total_size < other.total_size
    
    def add_file(self, file_name: str, file_size: int) -> None:
        self.files.append([file_name, file_size])
        cwd = self
        print("Adding a file")
        while cwd != None:
            print(cwd.dir_name)
            cwd.total_size += file_size
            cwd = cwd.parent
  
    def add_child(self, child: str) -> None:
        self.children.append(child)


def cd(tree: list[TreeNode], cwd: TreeNode, target_dir: str) -> TreeNode:
    if target_dir == "/":
        return [el for el in tree if el.dir_name == "/"][0]
    if target_dir == "..":
        return cwd.parent
    else: 
        return [el for el in tree if (el.dir_name == target_dir and cwd == el.parent)][0]


def mkdir(tree: list[TreeNode], cwd: TreeNode, target_dir: str) -> None:
    cwd.add_child(target_dir)
    tree.append(TreeNode(target_dir))


def line_is_command(line: str) -> bool:
    line = line.rstrip()
    if line.startswith('$'):
        return True
    return False


def perform_command(line: str, tree: list[TreeNode], cwd: TreeNode) -> TreeNode:
    command = line.split(' ')
    if command[1] == "ls":
        return cwd
    if command[1] == "cd":
        return cd(tree, cwd, command[2])


def check_output(line: str, tree: list[TreeNode], cwd: TreeNode) -> None:
    output = line.split(' ')
    if output[0] == "dir" and output[1] not in cwd.children:
        new_dir = TreeNode(output[1])
        new_dir.parent = cwd
        cwd.add_child(output[1])
        tree.append(new_dir)
    else:
        filesize = int(output[0])
        filename = output[1]
        if ([filename, filesize]) not in cwd.files:
            cwd.add_file(filename, filesize)      


def directory_to_delete(tree: list[TreeNode], total_space=70000000, required_unused_space=30000000) -> TreeNode:
    delete_space  =  tree[0].total_size + required_unused_space - total_space
    dir_big_enough = [el for el in tree if el.total_size > delete_space]
    dir_big_enough.sort()
    return dir_big_enough[0]


def main():
    with open(INPUT, "r") as f:
        tree_nodes = [TreeNode('/')]
        cwd = tree_nodes[0]
        for line in f:
            line = line.rstrip()
            if line_is_command(line):
                cwd = perform_command(line, tree_nodes, cwd)
            else:
                check_output(line, tree_nodes, cwd)
        
        print("Task1: total sum of small dirs")
        print(sum([el.total_size for el in tree_nodes if el.total_size < 100000]))

        print("Task2: size of dir to delete:")
        print(directory_to_delete(tree_nodes).total_size)


if __name__ == "__main__":
    main()