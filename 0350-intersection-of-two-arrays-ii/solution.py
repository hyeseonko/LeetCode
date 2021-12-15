class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        for num in nums1:
            if len(nums2)==0:
                break
            if num in nums2:
                nums2.remove(num)
                output.append(num)
        return output
                
        
