class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue=[[num] for num in nums]
        maxpool = math.factorial(len(nums))
        while(len(queue)<maxpool):
            curlist = queue.pop(0)
            # [1] -> [1,2] / [1,3]
            temp = list(set(nums).difference(set(curlist)))
            for t in temp:
                queue.append(curlist+[t])
        if len(nums)>1:
            for q in queue:
                temp = list(set(nums).difference(set(q)))
                q.append(temp[0])
        return queue
        
        