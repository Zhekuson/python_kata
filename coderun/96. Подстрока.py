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
    n, k = map(int, input().split())
    s = input()
    if n == 1:
        print(1, 1)
        return
    p1 = 0
    p2 = 0
    from collections import defaultdict
    cur_dict = defaultdict(lambda : 0)
    max_len = 0
    start_idx = 0
    while p1 <= p2 < len(s):
        cur_symb = s[p2]
        cur_dict[cur_symb] += 1
        if cur_dict[cur_symb] > k:
            if p2 - p1 > max_len:
                max_len = p2 - p1
                start_idx = p1
            while cur_dict[cur_symb] > k:
                cur_dict[s[p1]] -= 1
                p1 += 1
        p2 += 1
    if p1 != p2:
        if p2 - p1 > max_len:
            max_len = p2 - p1
            start_idx = p1
    print(max_len, start_idx+1)


if __name__ == '__main__':
    main()