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
    N, M = map(int, input().split())
    matrix = []
    for i in range(N):
        matrix.append([])
        matrix[i] = [*map(int, input().split())]

    for i in range(N):
        for j in range(M):
            if i >= 1:
                top = matrix[i - 1][j]
            else:
                top = 101 * 20
            if j >= 1:
                left = matrix[i][j - 1]
            else:
                left = 101 * 20

            if i == 0 and j == 0:
                top = 0
                left = 0
            matrix[i][j] = matrix[i][j] + min(top, left)
    # print(matrix)
    print(matrix[N - 1][M - 1])


if __name__ == '__main__':
    main()