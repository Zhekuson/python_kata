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
            post_len = pre_len + 1 + (1 if symb_length % 2 == 0 else 0)
            for item in current_level:
                if item[1] is not None:
                    print(' ' * pre_len + f'{item[1].value:^{symb_length}}' +
                          ' ' * post_len, end='')
                else:
                    print(' ' * pre_len + '-' * symb_length + ' ' * post_len, end='')
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
        return self._get_max()[0].value

    def _get_max(self, root=None):
        if root is None:
            root = self.root
        current = root
        parent = current
        while current.right_child is not None:
            parent = current
            current = current.right_child
        return current, parent

    def get_min(self):
        return self._get_min()[0].value

    def _get_min(self, root=None):
        if root is None:
            root = self.root
        current = root
        parent = current
        while current.left_child is not None:
            parent = current
            current = current.left_child
        return current, parent

    @staticmethod
    def __reassigning(parent, assigned_child, is_right_child):
        if is_right_child:
            parent.right_child = assigned_child
        else:
            parent.left_child = assigned_child

    def remove(self, value):
        current = self.root
        parent = None
        while current is not None:
            if value > current.value:
                if current.right_child is not None:
                    parent = current
                    current = current.right_child
                else:
                    return False
            elif value < current.value:
                if current.left_child is not None:
                    parent = current
                    current = current.left_child
                else:
                    return False
            else:

                if parent is None:
                    if current.right_child is not None:
                        min_node, local_parent = self._get_min(current.right_child)

                        min_node.right_child = current.right_child
                        min_node.left_child = current.left_child
                        local_parent.left_child = None
                        local_parent.right_child = min_node.right_child
                    elif current.left_child is not None:
                        max_node, local_parent = self._get_max(current.left_child)

                        max_node.right_child = current.right_child
                        max_node.left_child = current.left_child
                        local_parent.right_child = None
                        local_parent.left_child = max_node.left_child

                    current = None
                    return True
                else:
                    pred = (current.left_child is None, current.right_child is None)
                    is_right_child = False
                    if current.value > parent.value:
                        is_right_child = True
                    if pred[0] and pred[1]:
                        self.__reassigning(parent, None, is_right_child)
                    elif pred[0] and not pred[1]:
                        self.__reassigning(parent, current.right_child, is_right_child)
                    elif not pred[0] and pred[1]:
                        self.__reassigning(parent, current.left_child, is_right_child)
                    elif not pred[0] and not pred[1]:
                        if is_right_child:
                            # максимум слева
                            max_node, local_parent = self._get_max(current.left_child)
                            local_parent.right_child = None
                            max_node.right_child = current.right_child
                            max_node.left_child = current.left_child
                            parent.right_child = max_node
                        else:
                            # минимум справа
                            min_node, local_parent = self._get_min(current.right_child)
                            local_parent.left_child = None
                            min_node.right_child = current.right_child
                            min_node.left_child = current.left_child
                            parent.left_child = min_node
                    return True
        return False

    def pre_order(self, root: TreeNode = None):
        if root is None:
            root = self.root
        result = [root.value]
        if root.left_child is not None:
            result.extend(self.pre_order(root.left_child))
        if root.right_child is not None:
            result.extend(self.pre_order(root.right_child))
        return result

    def in_order(self, root: TreeNode = None):
        if root is None:
            root = self.root
        result = []
        if root.left_child is not None:
            result.extend(self.in_order(root.left_child))
        result.append(root.value)
        if root.right_child is not None:
            result.extend(self.in_order(root.right_child))
        return result

    def post_order(self, root: TreeNode = None):
        if root is None:
            root = self.root
        result = []
        if root.left_child is not None:
            result.extend(self.post_order(root.left_child))
        if root.right_child is not None:
            result.extend(self.post_order(root.right_child))
        result.append(root.value)
        return result

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
