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
            first_median = None
            p1, p2 = (lower_1 + upper_1) / 2, (lower_2 + upper_2) / 2

            if p1 >= 0 and (p2 < 0 or nums1[p1] >= nums2[p2]):
                if p2 + 1 == len(nums2) or nums1[p1] <= nums2[p2 + 1]:
                    p1_final_index = p1 + p2 + 1
                    if p1_final_index == first_median_index:
                        first_median = nums1[p1]
                    else:
                        if p1_final_index > first_median_index:
                            upper_1 = p1 - 1
                        else:
                            lower_1 = p1
                else:
                    lower_2 = p2 + 1
            else:
                if p1 + 1 == len(nums1) or nums1[p1 + 1] >= nums2[p2]:
                    p2_final_index = p1 + p2 + 1
                    if p2_final_index == first_median_index:
                        first_median = nums2[p2]
                    else:
                        if p2_final_index > first_median_index:
                            upper_2 = p2 - 1
                        else:
                            lower_2 = p2 + 1
                else:
                    lower_1 = p1 + 1
            if first_median is not None:
                if needs_second_median:
                    if p1 + 1 < len(nums1) and p2 + 1 < len(nums2):
                        second_median = nums2[p2 + 1] if nums2[p2 + 1] > nums1[p1 + 1] else nums1[p1 + 1]
                    elif p1 + 1 == len(nums1):
                        second_median = nums2[p2 + 1]
                    else:
                        second_median = nums1[p1 + 1]
                    return (first_median + second_median) / 2.0
                else:
                    return first_median


if __name__ == '__main__':
    nums1 = [2]
    nums2 = [1,3,4,5,6]
    print Solution().findMedianSortedArrays(nums1, nums2)
