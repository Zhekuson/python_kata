from data_structures.trees.TreeNode import TreeNode


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def print(self):
        depth_counter = self.get_depth()
        total_depth = depth_counter
        current_level = [(1, self.root)]
        symb_length = max(len(str(self.get_max())), len(str(self.get_min())))
        while depth_counter > 0:
            next_level = [(0, None)] * 2 ** (total_depth - depth_counter + 1)
            i = 0
            for node in current_level:
                if (node[0] == 1) and node[1].left_child is not None:
                    next_level[i] = (1, node[1].left_child)
                i += 1
                if (node[0] == 1) and node[1].right_child is not None:
                    next_level[i] = (1, node[1].right_child)
                i += 1
            pre_len = int(2 ** (depth_counter - 1) - 1) * (symb_length // 2 + 1)
            post_len = pre_len + 1
            for item in current_level:
                if item[1] is not None:
                    print(' ' * pre_len + f'{item[1].value:^{symb_length}}' +
                          ' ' * post_len, end='')
                else:
                    print(' ' * pre_len + '-'*symb_length + ' ' * post_len, end='')
            print()
            current_level = next_level
            depth_counter -= 1
        pass

    def insert(self, value):
        current = self.root
        while current is not None:
            if value > current.value:
                if current.right_child is not None:
                    current = current.right_child
                else:
                    node = TreeNode(value)
                    current.right_child = node
                    return
            else:
                if current.left_child is not None:
                    current = current.left_child
                else:
                    node = TreeNode(value)
                    current.left_child = node
                    return

    def search(self, value) -> bool:
        current = self.root
        while current is not None:
            if value > current.value:
                if current.right_child is not None:
                    current = current.right_child
                else:
                    return False
            elif value < current.value:
                if current.left_child is not None:
                    current = current.left_child
                else:
                    return False
            else:
                return True
        return False

    def get_max(self):
        current = self.root
        while current.right_child is not None:
            current = current.right_child
        return current.value

    def get_min(self):
        current = self.root
        while current.left_child is not None:
            current = current.left_child
        return current.value

    def remove(self, value):

        pass

    def pre_order(self, root: TreeNode = None):
        if root is None:
            root = self.root
        result = [root.value]
        if root.left_child is not None:
            result.append(self.pre_order(root.left_child))
        if root.right_child is not None:
            result.append(self.pre_order(root.right_child))
        return result

    def in_order(self):
        return

    def post_order(self):
        return

    def get_depth(self, root=None):
        if root is None:
            root = self.root
        depth = 1
        left_depth = 0
        right_depth = 0
        if root.left_child is not None:
            left_depth = self.get_depth(root.left_child)
        if root.right_child is not None:
            right_depth = self.get_depth(root.right_child)
        return depth + max(left_depth, right_depth)
