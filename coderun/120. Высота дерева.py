import sys


def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    arr = [*map(int, input().split())]

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    class BST:
        def __init__(self, root: Node):
            self.root = root

        def append_value(self, value: int, cur_node: Node):
            if value < cur_node.value:
                if cur_node.left is None:
                    cur_node.left = Node(value)
                else:
                    self.append_value(value, cur_node.left)
            elif value > cur_node.value:
                if cur_node.right is None:
                    cur_node.right = Node(value)
                else:
                    self.append_value(value, cur_node.right)

        def get_height(self, cur_node: Node):
            if cur_node.left is None:
                left_depth = 1
            else:
                left_depth = self.get_height(cur_node.left) + 1

            if cur_node.right is None:
                right_depth = 1
            else:
                right_depth = self.get_height(cur_node.right) + 1
            return max(left_depth, right_depth)

    root = Node(arr[0])
    bst = BST(root)

    for i in range(1, len(arr) - 1):
        bst.append_value(arr[i], bst.root)
    print(bst.get_height(bst.root))


if __name__ == '__main__':
    main()