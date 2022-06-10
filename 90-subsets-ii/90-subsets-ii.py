class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[[]]
        for num in nums:
            result += [i+[num] for i in result]
        result2=set()
        for res in result:
            target = tuple(sorted(res))
            result2.add(target)
        return result2