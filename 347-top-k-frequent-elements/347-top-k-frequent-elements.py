class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = [(num, nums.count(num)) for num in set(nums)]
        s_output = sorted(output, key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], s_output))[:k]