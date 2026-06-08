class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.bf = 0  # 平衡因子
    
    def __str__(self):
        return str(self.key)

class AVLTree:
    def __init__(self):
        self.root = None
        self.steps = []  # 记录每一步
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def update_height_and_bf(self, node):
        if not node:
            return
        left_h = self.get_height(node.left)
        right_h = self.get_height(node.right)
        node.height = 1 + max(left_h, right_h)
        node.bf = left_h - right_h
        return node.bf
    
    def right_rotate(self, y):
        """LL 右旋"""
        x = y.left
        T2 = x.right
        
        # 旋转
        x.right = y
        y.left = T2
        
        # 更新高度
        self.update_height_and_bf(y)
        self.update_height_and_bf(x)
        
        return x
    
    def left_rotate(self, x):
        """RR 左旋"""
        y = x.right
        T2 = y.left
        
        # 旋转
        y.left = x
        x.right = T2
        
        # 更新高度
        self.update_height_and_bf(x)
        self.update_height_and_bf(y)
        
        return y
    
    def get_balance_type(self, node):
        """判断失衡类型"""
        if node.bf > 1:  # 左子树高
            if node.left and node.left.bf >= 0:
                return "LL"
            else:
                return "LR"
        elif node.bf < -1:  # 右子树高
            if node.right and node.right.bf <= 0:
                return "RR"
            else:
                return "RL"
        return "balanced"
    
    def insert(self, root, key, step_num):
        """插入节点并保持平衡"""
        # 1. 普通BST插入
        if not root:
            return AVLNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key, step_num)
        elif key > root.key:
            root.right = self.insert(root.right, key, step_num)
        else:
            return root
        
        # 2. 更新高度和平衡因子
        self.update_height_and_bf(root)
        
        # 3. 检查是否失衡
        balance = root.bf
        
        # LL
        if balance > 1 and key < root.left.key:
            print(f"  步骤{step_num}: 节点{root.key}失衡，类型: LL，旋转轴: {root.left.key}")
            self.steps.append(f"步骤{step_num}: {root.key}失衡，LL右旋，轴={root.left.key}")
            return self.right_rotate(root)
        
        # RR
        if balance < -1 and key > root.right.key:
            print(f"  步骤{step_num}: 节点{root.key}失衡，类型: RR，旋转轴: {root.right.key}")
            self.steps.append(f"步骤{step_num}: {root.key}失衡，RR左旋，轴={root.right.key}")
            return self.left_rotate(root)
        
        # LR
        if balance > 1 and key > root.left.key:
            print(f"  步骤{step_num}: 节点{root.key}失衡，类型: LR")
            self.steps.append(f"步骤{step_num}: {root.key}失衡，LR (先左旋后右旋)")
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # RL
        if balance < -1 and key < root.right.key:
            print(f"  步骤{step_num}: 节点{root.key}失衡，类型: RL")
            self.steps.append(f"步骤{step_num}: {root.key}失衡，RL (先右旋后左旋)")
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def print_tree(self, node, level=0, prefix="根:"):
        """打印树形结构"""
        if node is not None:
            print("  " * level + f"{prefix} {node.key} (BF={node.bf}, H={node.height})")
            self.print_tree(node.left, level + 1, "L:")
            self.print_tree(node.right, level + 1, "R:")
    
    def inorder(self, node, result):
        """中序遍历验证BST性质"""
        if node:
            self.inorder(node.left, result)
            result.append(node.key)
            self.inorder(node.right, result)
        return result
    
    def build_from_sequence(self, seq):
        """从序列构建AVL树"""
        print("=" * 60)
        print(f"开始构建 AVL 树，插入序列: {seq}")
        print("=" * 60)
        
        for i, val in enumerate(seq, 1):
            print(f"\n第 {i} 步: 插入 {val}")
            print("-" * 40)
            self.root = self.insert(self.root, val, i)
            print(f"插入 {val} 后的树:")
            self.print_tree(self.root)
            print()
        
        print("\n" + "=" * 60)
        print("最终树的中序遍历:")
        inorder_result = self.inorder(self.root, [])
        print(f"{inorder_result}")
        print(f"BST性质验证: {inorder_result == sorted(seq)}")
        print("=" * 60)
        
        return self.root

# 运行实验
if __name__ == "__main__":
    # 给定的插入序列
    sequence = [38, 20, 10, 25, 40, 35, 50]
    
    # 创建AVL树并构建
    avl = AVLTree()
    avl.build_from_sequence(sequence)
    
    # 打印旋转步骤总结
    print("\n\n旋转步骤总结:")
    for step in avl.steps:
        print(f"  • {step}")