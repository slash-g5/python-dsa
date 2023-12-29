import sys
from functools import cmp_to_key

s = [1, 4, 5, 6, 6, 9, 1, 0, 1, 8]
s.sort()
print(s)
s.sort(reverse=True)
print(s)


def test_sort_helper(test_array):
    return test_array.left


def print_test_array(test_array):
    for a in test_array:
        a.print()
    print()


def custom_test_comparator(test1, test2):
    return (pow(test1.right, 2) + pow(test1.left, 2)) - (pow(test2.left, 2) + pow(test2.right, 2))


class Test:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self):
        sys.stdout.write(f'Test({self.left},{self.right}) ')
        sys.stdout.flush()


s = [Test(1, 1), Test(4, 1), Test(5, 6), Test(6, 9), Test(1, 0), Test(1, 8)]
s.sort(key=test_sort_helper)
print_test_array(s)

s.sort(key=test_sort_helper, reverse=True)
print_test_array(s)

s.sort(key=cmp_to_key(custom_test_comparator))
print_test_array(s)
