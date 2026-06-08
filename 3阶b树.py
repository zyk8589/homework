class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf          # 是否为叶子节点
        self.keys = []            # 键值列表（升序）
        self.children = []        # 子节点列表

class BTree:
    def __init__(self, t):
        self.t = t                # 最小度数（t = m/2 上取整，对于 m=3 阶，t=2）
        self.root = BTreeNode(leaf=True)
    
    def insert(self, k):
        root = self.root
        # 如果根节点已满，需要分裂
        if len(root.keys) == (2 * self.t - 1):
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(self.root, k)
        else:
            self._insert_non_full(root, k)
    
    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1
        
        if node.leaf:
            # 叶子节点：直接插入
            node.keys.append(0)
            while i >= 0 and node.keys[i] > k:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            # 非叶子节点：找到合适的子节点
            while i >= 0 and node.keys[i] > k:
                i -= 1
            i += 1
            
            # 如果子节点已满，先分裂
            if len(node.children[i].keys) == (2 * self.t - 1):
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)
    
    def _split_child(self, parent, i):
        t = self.t
        child = parent.children[i]
        new_child = BTreeNode(leaf=child.leaf)
        
        # 将 child 的后 t-1 个键移入 new_child
        parent.keys.insert(i, child.keys[t - 1])
        new_child.keys = child.keys[t:]
        child.keys = child.keys[:t - 1]
        
        # 如果不是叶子节点，子节点也要移动
        if not child.leaf:
            new_child.children = child.children[t:]
            child.children = child.children[:t]
        
        parent.children.insert(i + 1, new_child)
    
    def traverse(self):
        self._traverse(self.root, 0)
    
    def _traverse(self, node, level):
        indent = "    " * level
        print(f"{indent}节点(叶子={node.leaf}): {node.keys}")
        for child in node.children:
            self._traverse(child, level + 1)
    
    def print_tree(self):
        self._print_tree(self.root, "", True)
    
    def _print_tree(self, node, prefix, is_tail):
        # 打印当前节点的键值
        keys_str = " ".join(str(k) for k in node.keys)
        if node == self.root:
            print(f"根节点: [{keys_str}]")
        else:
            connector = "└── " if is_tail else "├── "
            print(f"{prefix}{connector}[{keys_str}]")
        
        # 更新前缀用于子节点
        if is_tail:
            prefix += "    "
        else:
            prefix += "│   "
        
        # 递归打印子节点
        for i, child in enumerate(node.children):
            is_last = (i == len(node.children) - 1)
            self._print_tree(child, prefix, is_last)


def main():
    # 创建 3 阶 B-Tree（t = ceil(3/2) = 2）
    btree = BTree(t=2)
    
    # 给定的键值序列
    keys = [10, 20, 5, 6, 12, 30, 25]
    
    print("依次插入:", keys)
    print("=" * 50)
    
    for key in keys:
        btree.insert(key)
        print(f"\n插入 {key} 后的树结构:")
        btree.print_tree()
        print("-" * 40)
    
    print("\n" + "=" * 50)
    print("最终 B-Tree 结构:")
    btree.print_tree()
    
    print("\n" + "=" * 50)
    print("详细遍历:")
    btree.traverse()


if __name__ == "__main__":
    main()