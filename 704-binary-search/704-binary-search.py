class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start=0
        end = len(nums)-1
        if nums[-1]==target:
            return end
        
        while(start!=end):
            cur=int((start+end)/2)
            if nums[cur]==target:
                return cur
            elif nums[cur]<target:
                if start==cur:
                    break
                start=cur
            else:
                if end==cur:
                    break
                end=cur
        return -1