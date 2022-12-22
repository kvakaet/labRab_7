#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

# 4. В списке, состоящем из вещественных элементов, вычислить:
# 1. сумму элементов списка с нечетными номерами;
# 2. сумму элементов списка, расположенных между первым и последним отрицательными
# элементами.
# Сжать список, удалив из него все элементы, модуль которых не превышает 1. Освободившиеся в
# конце списка элементы заполнить нулями.

if __name__ == "__main__":
    lst = list(map(float, input("Enter the list of float numbers: ").split(" ")))

    print([item for i, item in enumerate(lst) if i % 2 != 0])

    start = 0
    finish = -1

    for i, item in enumerate(lst):
        if item < 0:
            start = i
            break
    for i, item in enumerate(lst, -1):
        if item < 0:
            finish = i
            break

    print(sum(lst[start + 1: finish]))

    for i, item in enumerate(lst):
        if math.fabs(item) <= 1:
            lst.pop(i)
            lst.insert(i, 0)
    lst.sort(key=lambda x: x == 0)

    print(lst)
