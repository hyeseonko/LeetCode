class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        # method 2. Recursive
        if 0<=start<len(arr) and arr[start]>=0:
            arr[start]=-arr[start] # visited flag
            return arr[start]==0 or self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])
        return False
        
        # method 1. BFS
        # queue = [start]
        # length = len(arr)
        # while queue:
        #     cur = queue.pop(0)
        #     if arr[cur]==0:
        #         return True
        #     if cur + arr[cur] in range(length) and arr[cur+arr[cur]]!=-1:
        #         queue.append(cur+arr[cur])
        #     if cur - arr[cur] in range(length) and arr[cur-arr[cur]]!=-1:
        #         queue.append(cur-arr[cur])           
        #     arr[cur] = -1
        # return False