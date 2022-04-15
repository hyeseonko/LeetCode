class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dp=[s[0]]
        last = 0 # updated
        for i, each in enumerate(s[1:], 1):
            if each not in dp[-1]:
                dp.append(dp[-1]+each)
            else:
                last_idx = s[:i][::-1].index(each)
                dp.append(s[i-last_idx:i+1])
        return len(max(dp, key=len))
        