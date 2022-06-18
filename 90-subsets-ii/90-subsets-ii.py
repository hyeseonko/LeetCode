class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # result=[[]]
        # for num in nums:
        #     result += [i+[num] for i in result]
        # result2=set()
        # for res in result:
        #     result2.add(tuple(sorted(res)))
        # return result2
        
        def backtrack(path, index):
            output.add(tuple(sorted(path)))
            if len(nums)==len(path):
                return
            
            for i in range(index, len(nums)):
                # add
                path.append(nums[i])
                # go next
                backtrack(path, i+1)
                # backtrack
                path.pop()
        output = set()
        backtrack([], 0)
        return output