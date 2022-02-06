class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[(temperatures[0],0)]
        N = len(temperatures)
        output=[0]*N
        for i in range(1, N):
            cur, idx = stack[-1]
            if cur < temperatures[i]:
                output[idx]=i-idx
                stack.pop(-1)
                while(stack and stack[-1][0]<temperatures[i]):
                    output[stack[-1][1]]=i-stack[-1][1]
                    stack.pop(-1)
            stack.append((temperatures[i], i))
        return output