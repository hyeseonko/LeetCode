class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # BFS
        queue = [start]
        length = len(arr)
        while queue:
            cur = queue.pop(0)
            if arr[cur]==0:
                return True

            if cur + arr[cur] in range(length) and arr[cur+arr[cur]]!=-1:
                queue.append(cur+arr[cur])
            if cur - arr[cur] in range(length) and arr[cur-arr[cur]]!=-1:
                queue.append(cur-arr[cur])           
            
            arr[cur] = -1
            
        return False