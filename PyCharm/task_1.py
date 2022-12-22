#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    A = [int(i) for i in input("введите аценки по алгебре\n").split(" ")]
    G = [int(i) for i in input("введите аценки по геометрии\n").split(" ")]
    F = [int(i) for i in input("введите аценки по физике\n").split(" ")]
    count = 0

    for i, grade in enumerate(A):
        student = [A[i], G[i], F[i]]

        # определение количества учеников без 2
        if 2 not in student:
            count += 1

    # средняя оценка по алгебре
    mean = sum(A) / len(A)

    print(f"количество учеников без двоек = {count}\nсредняя оценка по алгебре = {mean}")
