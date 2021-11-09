from test_framework import generic_test


def power(x: float, y: int) -> float:
    if y == 0: return 1
    elif y == 1: return x

    result = 1
    xAbs, yAbs = abs(x), abs(y)
    for i in range(yAbs):
        result *= xAbs
    
    if y < 0: result = 1 / result
    if x < 0 and abs(y) % 2 != 0: result *= -1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
