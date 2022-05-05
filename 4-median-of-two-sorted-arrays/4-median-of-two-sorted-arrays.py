class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1)+len(nums2)
        snums = sorted(nums1+nums2)
        return snums[total_len//2] if total_len%2==1 else (snums[total_len//2]+snums[total_len//2-1])*0.5