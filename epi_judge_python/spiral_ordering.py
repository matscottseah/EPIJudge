from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    spiral = []
    iMin = jMin = 0
    iMax = jMax = len(square_matrix) - 1

    iterations = (len(square_matrix) * 2) -1
    step = 0

    for i in range(iterations):
        currentSpiral = []
        if step % 4 == 0:
            for j in range(jMin, jMax + 1):
                currentSpiral.append(square_matrix[iMin][j])
            iMin += 1
        elif step % 4 == 1:
            for i in range(iMin, iMax + 1):
                currentSpiral.append(square_matrix[i][jMax])
            jMax -= 1
        elif step % 4 == 2:
            for j in range(jMax, jMin - 1, -1):
                currentSpiral.append(square_matrix[iMax][j])
            iMax -= 1
        else:
            for i in range(iMax, iMin - 1, -1):
                currentSpiral.append(square_matrix[i][jMin])
            jMin += 1
        spiral += currentSpiral
        step += 1

    return spiral


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
