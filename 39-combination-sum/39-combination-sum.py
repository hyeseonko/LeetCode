class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        candidates.sort()
        
        def backtrack(target, index, path):
            if target<0:
                return
            if target==0:
                output.append(path[:])
                return
            for i in range(index, len(candidates)):
                backtrack(target-candidates[i], i, path+[candidates[i]])
        
        backtrack(target, 0, [])
        return output
        
        
        
        
        
        
#         res = []
#         candidates.sort()
        
#         def dfs(target, index, path):
#             if target < 0:
#                 return  # backtracking
#             if target == 0:
#                 res.append(path)
#                 return 
#             for i in range(index, len(candidates)):
#                 dfs(target-candidates[i], i, path+[candidates[i]])
        
#         dfs(target, 0, [])
#         return res