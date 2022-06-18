class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # method 1. backtrack (recursive)
        # def backtrack(path, index):
        #     if len(path)==k:
        #         output.append(path[:])
        #         return
        #     for i in range(index, n+1):
        #         # add
        #         path.append(i)
        #         # go next
        #         backtrack(path, i+1)
        #         # backtrack
        #         path.pop()
        # output = []
        # backtrack([], 1)
        # return output
        
        # method 2. python function - combinations
        from itertools import combinations
        return list(combinations(range(1, n+1), k))