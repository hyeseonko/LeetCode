class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # method 1. O(N) time O(N) space
        # N = len(nums) - 1
        # seen = [0] * (N+1)
        # for num in nums:
        #     if seen[num]:
        #         return num
        #     seen[num] =1
        
        # method 2. O(N) time O(1) space: Negative Marking
        for num in nums:
            cur = abs(num)
            if nums[cur]<0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]
        
        # restore numbers
        for i in range(len(nums)):
            nums[i]=abs(nums[i])
        return duplicate
        
        # method 3. O(NlogN) time O(1) space: binary search
        # N = len(nums) - 1
        # lo, hi = 1, N
        # while lo < hi:
        #     mi = ( lo + hi ) >> 1
        #     less, equal = 0, 0
        #     for num in nums:
        #         if num < mi:
        #             less += 1
        #         elif num == mi:
        #             equal += 1
        #     if equal > 1:
        #         return mi
        #     if less >= mi:
        #         hi = mi - 1
        #     else:
        #         lo = mi + 1
        # return lo
        
        # method 3. Two pointers (Tortoise and Hare)
        
        
        
        # method 4. sorting O(NlogN)
        # prev = -1
        # for num in sorted(nums):
        #     if prev == num:
        #         return num
        #     prev = num
        
        # Reference: https://leetcode.com/problems/find-the-duplicate-number/discuss/705111/summary-7-solutions-%2B-consice-explanation-and-complexity-analysis