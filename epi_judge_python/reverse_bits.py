from test_framework import generic_test


def reverse_bits(x: int) -> int:
    result, num = 0, x
    while num:
        result <<= 1
        if num & 1: result += 1
        num >>= 1
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
