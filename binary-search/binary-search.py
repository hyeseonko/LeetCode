class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end = len(nums)-1
        if nums[0]==target:
            return 0
        while(start!=end):
            cur=int((start+end)/2)
            if nums[cur]==target:
                return cur
            elif nums[start]==target:
                return start
            elif nums[end]==target:
                return end
            elif nums[cur]<target:
                if start==cur:
                    break
                start=cur
            else:
                if end==cur:
                    break
                end=cur
        return -1
        