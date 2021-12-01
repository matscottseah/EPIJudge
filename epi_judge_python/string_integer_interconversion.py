from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string

def int_to_string(x: int) -> str:
    result = []
    num, negative = abs(x), False if x >= 0 else True
    while num:
        result.insert(0, chr(ord('0') + num % 10))
        num //= 10

    if negative:
        result.insert(0, '-')

    return ''.join(result) if len(result) > 0 else '0'


def string_to_int(s: str) -> int:
    i, sign = 0, 1
    if s[0] == '-':
        i, sign = 1, -1
    elif s[0] == '+':
        i = 1
    
    result = 0
    while i < len(s):
        result = (result * 10) + string.digits.index(s[i])
        i += 1

    return result * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
