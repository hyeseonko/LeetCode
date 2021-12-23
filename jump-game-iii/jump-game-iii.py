class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # BFS
        visited = [False]*len(arr)
        stack=[start]
        visited[start]=True
        
        # while stack is not empty
        while(stack):
            cur_idx = stack.pop(0)
            if arr[cur_idx]==0:
                return True
            plus_idx = cur_idx+arr[cur_idx]
            minus_idx = cur_idx-arr[cur_idx]

            if plus_idx < len(arr) and not visited[plus_idx]:
                stack.append(plus_idx)
                visited[plus_idx]=True
            if minus_idx >= 0 and not visited[minus_idx]:
                stack.append(minus_idx)
                visited[minus_idx]=True
        return False