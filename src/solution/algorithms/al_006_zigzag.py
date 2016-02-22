class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = []
        for row in range(numRows):
            go_down = False
            next_index = row
            while next_index < len(s):
                result.append(s[next_index])
                if (go_down and row != 0) or (not go_down and row != numRows - 1):
                    go_down = not go_down
                if go_down:
                    next_index += (numRows - row - 1) * 2
                else:
                    next_index += row * 2

        import string
        return string.join(result, '')


import unittest


class TestSolution(unittest.TestCase):
    def test_solution(self):
        print Solution().convert('A', 1)
#PAHNAPLSIIGYIR