class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_32_max = 2147483647
        int_32_min = -int_32_max - 1
        positive = 1 if x >= 0 else -1
        x *= positive
        result = 0
        while x is not 0:
            digit = x % 10
            if result != 0:
                if int_32_max/result < 10 or int_32_max - result * 10 < digit \
                        or int_32_min/-result < 10 or int_32_min + result * 10 > -digit:
                    return 0
            result = result * 10 + digit
            x /= 10
        return result * positive

import unittest


class TestSolution(unittest.TestCase):
    def test_solution(self):
        print Solution().reverse(-7463847412)

