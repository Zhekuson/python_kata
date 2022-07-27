from __future__ import annotations

from typing import List

import numpy as np


def quick_sort(a: List | np.ndarray) -> List | np.ndarray:
    N = len(a)
    if N == 0:
        return []
    elif N == 1:
        return a
    elif N == 2:
        return [a[0], a[1]] if a[0] < a[1] else [a[1], a[0]]
    pivot = a[N // 2]
    left = []
    right = []
    counter = 0
    for j in range(N):
        if a[j] < pivot:
            left.append(a[j])
        elif a[j] > pivot:
            right.append(a[j])
        else:
            counter += 1
    left = quick_sort(left)
    left.extend(counter * [pivot])

    right = quick_sort(right)
    left.extend(right)
    return left


if __name__ == '__main__':

    for i in range(10000):
        arr = np.random.randint(-100, 101, 20)
        if i % 100 == 0:
            print(arr)
            print(quick_sort(arr))
        assert np.allclose(sorted(arr), quick_sort(arr))
