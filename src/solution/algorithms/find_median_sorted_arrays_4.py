class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        first_median_index = (len(nums1) + len(nums2) - 1) / 2
        needs_second_median = (len(nums1) + len(nums2)) % 2 == 0

        lower_1, upper_1 = 0, len(nums1) - 1
        lower_2, upper_2 = 0, len(nums2) - 1

        while True:
            p1, p2 = (lower_1 + upper_1) / 2, (lower_2 + upper_2) / 2
            if p2 < 0 or nums1[p1] < nums2[p2]:
                p1_at_most_index = p1 + p2
                if (p2 == 0 or nums1[p1] > nums2[p2 - 1]) and p1_at_most_index == first_median_index:
                    first_median = nums1[p1]
                    if needs_second_median:
                        second_median = nums1[p1 + 1] if (p1 + 1) < len(nums1) and nums1[p1 + 1] < nums2[p2] else nums2[p2]
                        return (first_median + second_median) / 2.0
                    else:
                        return first_median
                else:
                    if p1_at_most_index > first_median_index:
                        lower_1 = p1 + 1
                    else:
                        upper_2 = p2
            else:
                p2_at_most_index = p1 + p2
                if (p1 == 0 or nums2[p2] <= nums1[p1 - 1]) and p2_at_most_index == first_median_index:
                    first_median = nums2[p2]
                    if needs_second_median:
                        second_median = nums2[p2 + 1] if (p2 + 1) < len(nums2) and nums2[p2 + 1] <= nums1[p1] else nums1[p1]
                        return (first_median + second_median) / 2.0
                    else:
                        return first_median
                else:
                    if p2_at_most_index > first_median_index:
                        lower_2 = p2 + 1
                    else:
                        upper_1 = p1


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print Solution().findMedianSortedArrays(nums1, nums2)
