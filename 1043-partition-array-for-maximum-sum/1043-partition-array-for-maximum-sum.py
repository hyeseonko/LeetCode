class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp=[max(arr[0:1+i])*(i+1) for i in range(k)]
        for i in range(k, len(arr)):
            cur = 0
            for window in range(k):
                cur = max(cur, dp[i-k+window]+max(arr[i-k+1+window:i+1])*(k-window))
            dp.append(cur)
        return dp[-1]