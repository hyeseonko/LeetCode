class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for num in nums1:
            idx = nums2.index(num)
            target = -1
            for n in nums2[idx+1:]:
                if n>num:
                    target = n
                    break
            output.append(target)
        return output