import sys


def main():
    n, r = map(int, input().split())
    dist_arr = list(map(int, input().split()))
    p1 = 0
    p2 = 1
    total_sum = 0
    while p2 < n and p1 < n:
        while p2 < n and dist_arr[p2] - dist_arr[p1] <= r:
            p2 += 1
        total_sum += 1 * (n - p2)
        p1 += 1
    print(total_sum)


if __name__ == '__main__':
    main()