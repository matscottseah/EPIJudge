from test_framework import generic_test


def parity(x: int) -> int:
    numBits = 0
    while x:
        numBits += x & 1
        x >>= 1
    return 0 if numBits % 2 == 0 else 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
