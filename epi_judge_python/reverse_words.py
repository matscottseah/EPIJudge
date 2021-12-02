import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].

def reverse_words(s):
    def reverseWord(left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    reverseWord(0,len(s) - 1)

    begin = end = 0
    while end < len(s):
        if s[end] == ' ':
            reverseWord(begin, end - 1)
            begin = end = end + 1
        else:
            end += 1

    reverseWord(begin, end - 1)

    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
