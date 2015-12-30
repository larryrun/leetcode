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
            first_median, second_median = None, None
            p1 = (lower_1 + upper_1) / 2
            p2 = (lower_2 + upper_2) / 2

            if p1 >= 0 and (p2 < 0 or nums1[p1] >= nums2[p2]):
                p1_at_least_index = p1 + p2 + 1
                if p1_at_least_index > first_median_index:
                    upper_1 = max(p1 - 1, 0)

                p2_at_most_index = p1_at_least_index - 1
                if p2_at_most_index < first_median_index:
                    lower_2 = min(p2 + 1, len(nums2) - 1)

                if p2 + 1 >= len(nums2) or nums1[p1] <= nums2[p2 + 1]:
                    p1_final_index = p1_at_least_index
                    if p1_final_index < first_median_index:
                        lower_1 = min(p1 + 1, len(nums1) - 1)
                    elif p1_final_index == first_median_index:
                        first_median = nums1[p1]
                        if needs_second_median:
                            second_median = nums1[p1 + 1] if p1 + 1 < len(nums1) and ((p2 + 1) >= len(nums2) or nums1[p1 + 1] < nums2[p2 + 1]) else nums2[p2 + 1]
                            return (first_median + second_median) / 2.0
                        else:
                            return first_median
                if p1 == 0 or nums1[p1 - 1] <= nums2[p2]:
                    p2_final_index = p2_at_most_index
                    if p2_final_index > first_median_index:
                        upper_2 = p2 - 1
                    elif p2_final_index == first_median_index:
                        first_median = nums2[p2]
                        if needs_second_median:
                            second_median = nums1[p1] if (p2 + 1) >= len(nums2) or nums1[p1] < nums2[p2 + 1] else nums2[p2 + 1]
                            return (first_median + second_median) / 2.0

            else:
                p2_at_least_index = p1 + p2 + 1
                if p2_at_least_index > first_median_index:
                    upper_2 = max(p2 - 1, 0)

                p1_at_most_index = p2_at_least_index - 1
                if p1_at_most_index < first_median_index:
                    lower_1 = min(p1 + 1, len(nums1) - 1)

                if p1 + 1 >= len(nums1) or nums2[p2] <= nums1[p1 + 1]:
                    p2_final_index = p2_at_least_index
                    if p2_final_index < first_median_index:
                        lower_2 = min(p2 + 1, len(nums2) - 1)
                    elif p2_final_index == first_median_index:
                        first_median = nums2[p2]
                        if needs_second_median:
                            second_median = nums1[p1 + 1] if p1 + 1 < len(nums1) and ((p2 + 1) >= len(nums2) or nums1[p1 + 1] < nums2[p2 + 1]) else nums2[p2 + 1]
                            return (first_median + second_median) / 2.0
                        else:
                            return first_median
                if p2 == 0 or nums2[p2 - 1] <= nums1[p1]:
                    p1_final_index = p1_at_most_index
                    if p1_final_index > first_median_index:
                        upper_1 = p1 - 1
                    elif p1_final_index == first_median_index:
                        first_median = nums1[p1]
                        if needs_second_median:
                            second_median = nums2[p2] if (p1 + 1) >= len(nums1) or nums2[p2] < nums1[p1 + 1] else nums1[p1 + 1]
                            return (first_median + second_median) / 2.0
                        else:
                            return first_median

            if first_median is not None:
                if needs_second_median:
                    return (first_median + second_median) / 2.0
                else:
                    return first_median / 1.0


if __name__ == '__main__':
    nums1 = [2]
    nums2 = [1,3,4]
    print Solution().findMedianSortedArrays(nums1, nums2)
