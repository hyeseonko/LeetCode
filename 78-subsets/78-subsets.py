class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # method 1. cascading
        # output = [[]]
        # for num in nums:
        #     output += [o + [num] for o in output]
        # return output
        
        # method 2. backtracking
        def backtrack(first=0, curr=[]):
            if len(curr)==k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # step 1. add nums[i] to curr
                curr.append(nums[i])
                # step 2. go next
                backtrack(i+1, curr)
                # step 3. backtrack
                curr.pop()
        output = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
            
        return output