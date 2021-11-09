from test_framework import generic_test


def parity(x: int) -> int:
    parity = 0
    while x:
        x = x&(x-1)
        parity ^= 1
    return parity


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
