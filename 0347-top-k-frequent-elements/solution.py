class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0)+1
        
        sorted_cnt = sorted(cnt, key=cnt.get, reverse=True)
        return sorted_cnt[:k]
