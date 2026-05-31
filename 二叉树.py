class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_from_array(arr):
    if not arr or arr[0] is None:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in arr]

    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(nodes):
                nodes[i].right = nodes[right_idx]
    
    return nodes[0]

def print_tree_visual(root):
    lines = _build_tree_string(root, 0, False, "-")[0]
    for line in lines:
        print(line)

def _build_tree_string(root, curr_index, is_right, label):
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    node_repr = str(root.val)
    new_root_width = gap_size = len(node_repr)

    l_box, l_box_width, l_box_height, l_box_start = _build_tree_string(root.left, 2*curr_index+1, False, "-")
    r_box, r_box_width, r_box_height, r_box_start = _build_tree_string(root.right, 2*curr_index+2, True, "-")

    if l_box_width > 0:
        l_root = int((l_box_start + l_box_width / 2))
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    if r_box_width > 0:
        r_root = int(r_box_start)
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1

    new_root_width += l_box_width + r_box_width
    gap = ' ' * gap_size

    new_line1 = ''.join(line1)
    new_line2 = ''.join(line2)
    l_index = new_root_start
    r_index = new_root_start + len(node_repr) + gap_size - 1 if r_box_width > 0 else 0

    l_box = [line if i < len(l_box) else ' ' * l_box_width for i, line in enumerate(l_box)]
    r_box = [line if i < len(r_box) else ' ' * r_box_width for i, line in enumerate(r_box)]

    tree = [new_line1, new_line2]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        tree.append(l_line + gap + r_line)

    return tree, new_root_width, len(tree), new_root_start

arr = [10, 5, 15, 3, 7, None, 20]
root = build_tree_from_array(arr)
print_tree_visual(root)



