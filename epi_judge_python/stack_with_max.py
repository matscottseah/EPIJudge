from typing import NamedTuple
from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections


class Stack:
    elementWithMax = collections.namedtuple('elementWithMax', ('element', 'max'))

    def __init__(self) -> None:
        self.stack: list[Stack.elementWithMax] = []

    def empty(self) -> bool:
        return len(self.stack) == 0

    def max(self) -> int:
        return self.stack[-1].max

    def pop(self) -> int:
        return self.stack.pop().element

    def push(self, x: int) -> None:
        self.stack.append(Stack.elementWithMax(x, x if self.empty() else max(x, self.max())))
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
