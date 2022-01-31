class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.start = Node(None)
        self.end = Node(None)

    def insert(self, index, value):
        i = 0
        cur_node = self.start
        while i < index:
            cur_node = cur_node.next
            i += 1
        ins_node = Node(value)
        if cur_node.next is not None:
            next_node = cur_node.next
        else:
            next_node = self.end

        cur_node.next = ins_node
        ins_node.prev = cur_node

        ins_node.next = next_node
        next_node.prev = ins_node

    def remove_at(self, index):
        i = 0
        cur_node = self.start
        while i <= index:
            cur_node = cur_node.next
            i += 1
        prev_node = cur_node.prev if cur_node.prev is not None else self.start
        next_node = cur_node.next if cur_node.next is not None else self.end
        prev_node.next = next_node
        next_node.prev = prev_node
        del cur_node

    def __str__(self):
        cur_node = self.start
        result = 'start'
        while cur_node.next is not self.end:
            cur_node = cur_node.next
            result += ' <-> {0}'.format(cur_node.value)
        result += ' <-> end'
        return result



