class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_start, max_len = 0, 1
        for i in range(0, len(s)):
            j = len(s) - 1
            while j > i:
                j -= 1
                if s[j] == s[i]:
                    j_start_at = j
                    j -= 1
                    while j > i and s[j] == s[i + j_start_at - j]:
                        j -= 1
                    if j == i or j == i + 1:
                        seq_len = j_start_at - i + 1
                        if seq_len > max_len:
                            max_start = i
                            max_len = seq_len
        return s[max_start: max_start + max_len]


import unittest


class TestSolution(unittest.TestCase):
    def test_solution(self):
        s = 'aaabaaaa'
        self.assertEqual('aaabaaa', Solution().longestPalindrome(s))
