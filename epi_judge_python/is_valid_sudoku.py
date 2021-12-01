from typing import List
from math import sqrt

from test_framework import generic_test
def hasDuplicates(nums: List[int]) -> bool:
    if len(set(filter(lambda num: num != 0, nums))) != len(list(filter(lambda num: num != 0, nums))):
        return True
    else:
        return False

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # row
    for i in range(len(partial_assignment)):
        if hasDuplicates(partial_assignment[i]):
            return False

    #column
    for j in range(len(partial_assignment)):
        column = [row[j] for row in partial_assignment]
        if hasDuplicates(column):
            return False

    #subgrid
    i = j = 0
    for _ in range(len(partial_assignment)):
        nums = []
        regionSize = int(sqrt(len(partial_assignment)))
        for offset in range(regionSize):
            nums += partial_assignment[i + offset][j:j+regionSize]
        if hasDuplicates(nums):
            return False
        
        if j == len(partial_assignment) - regionSize:
            i += regionSize
            j = 0
        else:
            j += regionSize

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
