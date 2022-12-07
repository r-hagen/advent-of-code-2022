from anytree import Node, RenderTree, findall

lines = [line.strip() for line in open('d07input.txt').readlines()]
lines.pop(0)
root = Node('/')

pwd = root
for line in lines:
    if '$ cd /' in line:
        pwd = root
    elif '$ cd ..' in line:
        pwd = pwd.parent
    elif '$ cd ' in line:
        d = Node(line.removeprefix('$ cd '), parent=pwd)
        pwd = d
    elif '$ ls' in line:
        continue
    elif line.startswith('dir'):
        d = Node(line.removeprefix('dir '), parent=pwd)
    else:
        (size, name) = line.split()
        f = Node(name, parent=pwd, size=int(size))

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))


def dir_size(node: Node):
    if node.is_leaf and 'size' in node.__dict__:
        return node.size
    return sum([dir_size(child) for child in node.children])


used_space = dir_size(root)
candidates = []
for directory in findall(root, filter_=lambda x: x.is_leaf is False):
    size = dir_size(directory)
    if 70000000 - used_space + size >= 30000000:
        candidates.append((directory, size))
candidates.sort(key=lambda t: t[1])
print(candidates[0])
