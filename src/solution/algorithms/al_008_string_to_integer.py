class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -MAX_INT - 1
        stat = 'BEFORE'
        sign = 1
        result = 0
        for c in str:
            if c != ' ' and stat == 'BEFORE':
                if c in '-+':
                    sign = 1 if c == '+' else -1
                    stat = 'NUM'
                    continue
                else:
                    stat = 'NUM'
            if stat == 'NUM' and c not in '0123456789':
                break
            if stat == 'NUM':
                num = '0123456789'.find(c)
                if result != 0:
                    if sign == 1 and (MAX_INT/result < 10 or MAX_INT - result * 10 < num):
                        return MAX_INT
                    if sign == -1 and (MIN_INT/(-result) < 10 or MIN_INT + result * 10 > -num):
                        return MIN_INT
                result = result * 10 + num
        return result * sign


import unittest


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(123, Solution().myAtoi('   +123'))
        self.assertEqual(-123, Solution().myAtoi('   -123'))
        self.assertEqual(-123, Solution().myAtoi('   -123abcd'))
        self.assertEqual(2147483647, Solution().myAtoi(' 2147483648'))
        self.assertEqual(-2147483648, Solution().myAtoi(' -2147483649  '))
        self.assertEqual(-2147483647, Solution().myAtoi('-2147483647'))


