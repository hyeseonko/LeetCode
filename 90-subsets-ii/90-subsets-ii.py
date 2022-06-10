class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[[]]
        for num in nums:
            result += [i+[num] for i in result]
        result2=set()
        for res in result:
            result2.add(tuple(sorted(res)))
        return result2