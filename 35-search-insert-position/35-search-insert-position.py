class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        if target<=nums[start]: return 0
        elif target>nums[end-1]: return end
        else:
            while(start<end):
                mid = (start+end)//2
                if target<=nums[mid] and nums[mid-1]<target:
                    return mid
                elif target>nums[mid]:
                    start=mid+1
                elif target<=nums[mid-1]:
                    end=mid-1
            return start