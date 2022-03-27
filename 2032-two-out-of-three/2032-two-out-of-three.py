class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        output=[]
        for num in set(nums1+nums2+nums3):
            if num in nums1 and num in nums2:
                output.append(num)
            elif num in nums1 and num in nums3:
                output.append(num)
            elif num in nums2 and num in nums3:
                output.append(num)
            else:
                continue
        return output