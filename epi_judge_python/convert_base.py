from test_framework import generic_test

strToInt = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

intToStr = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    if num_as_string == '0':
        return '0'

    negative = True if num_as_string[0] == '-' else False
    decimal = 0

    for i in range(len(num_as_string)):
        if num_as_string[len(num_as_string) - 1 - i] == '-':
            break
        decimal += (strToInt[num_as_string[len(num_as_string) - 1 - i]] * (b1 ** i))

    result = []
    while decimal:
        result.append(intToStr[decimal % b2])
        decimal //= b2

    return ('-' if negative else '') + ''.join(reversed(result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
