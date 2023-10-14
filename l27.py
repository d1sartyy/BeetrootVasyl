class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)

class BinaryTree:

    def __init__(self, root_node: BinaryTreeNode = None):
        self.root = root_node

    def insert(self, value):
        current_root = self.root
        while True:
            if current_root.value < value:
                if current_root.right:
                    current_root = current_root.right
                else:
                    new_node = BinaryTreeNode(value)
                    current_root.right = new_node
                    break
            elif current_root.value > value:
                if current_root.left:
                    current_root = current_root.left
                else:
                    new_node = BinaryTreeNode(value)
                    current_root.left = new_node
                    break
            else:
                break

    def insert_tree(self, tree):
        if not tree.root:
            return
        self._recursive_insert(self.root, tree.root)

    def _recursive_insert(self, current_node, tree_node):
        if current_node.value < tree_node.value:
            if current_node.right:
                self._recursive_insert(current_node.right, tree_node)
            else:
                current_node.right = tree_node
        elif current_node.value > tree_node.value:
            if current_node.left:
                self._recursive_insert(current_node.left, tree_node)
            else:
                current_node.left = tree_node

    def remove_subtree(self, value):
        self.root = self._recursive_remove_subtree(self.root, value)

    def _recursive_remove_subtree(self, current_node, value):
        if current_node is None:
            return None
        if current_node.value < value:
            current_node.right = self._recursive_remove_subtree(current_node.right, value)
        elif current_node.value > value:
            current_node.left = self._recursive_remove_subtree(current_node.left, value)
        else:
            current_node = None
        return current_node

    @staticmethod
    def create_from_list(l: list):
        root_node = BinaryTreeNode(l[0])
        binary_tree = BinaryTree(root_node)
        for value in l[1:]:
            binary_tree.insert(value)
        return binary_tree

    def is_value_in_tree(self, value) -> bool:
        pass

    def in_order_traversal(self, node):
        if node is None:
            return []
        left = self.in_order_traversal(node.left)
        right = self.in_order_traversal(node.right)
        return left + [node.value] + right


    def display_in_order(self):
        result = self.in_order_traversal(self.root)
        print(' '.join(map(str, result)))


number_list = [6, 25, 11, 28, 15, 12, 19, 24, 22, 9, 1, 0, 26, 24, 28, 1, 28, 15, 2, 13, 8, 22, 27, 19, 7]
binary_tree = BinaryTree.create_from_list(number_list)
binary_tree.display_in_order()

new_tree = BinaryTree.create_from_list([14, 10, 20, 5, 12, 17, 25])
binary_tree.insert_tree(new_tree)
binary_tree.display_in_order()

binary_tree.remove_subtree(25)
binary_tree.display_in_order()




