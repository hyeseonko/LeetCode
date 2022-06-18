class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # method 1. Naive
        # queue=[[num] for num in nums]
        # maxpool = math.factorial(len(nums))
        # while(len(queue)<maxpool):
        #     curlist = queue.pop(0)
        #     # [1] -> [1,2] / [1,3]
        #     temp = list(set(nums).difference(set(curlist)))
        #     for t in temp:
        #         queue.append(curlist+[t])
        # if len(nums)>1:
        #     for q in queue:
        #         temp = list(set(nums).difference(set(q)))
        #         q.append(temp[0])
        # return queue
        
        # method 2. backtrack
        def backtrack(path, visited, output):
            if len(path)==len(nums):
                output.append(path[:])
                return
            
            for i, num in enumerate(nums):
                if visited[i]:
                    continue
                # add
                path.append(num)
                visited[i]=True
                # go next
                backtrack(path, visited, output)
                # pop
                path.pop()
                visited[i]=False

        output = []
        backtrack([], [False]*len(nums),output)
        return output
        
        
        