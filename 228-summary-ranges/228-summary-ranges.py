class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        if nums:
            cur = [nums[0]]
            for num in nums[1:]:
                if cur[-1]+1!=num:
                    if len(cur)==1:
                        output.append(str(cur[-1]))
                    else:
                        output.append(str(cur[0])+"->"+str(cur[-1]))
                    cur = []
                cur.append(num)
            if len(cur)==1:
                output.append(str(cur[-1]))
            else:
                output.append(str(cur[0])+"->"+str(cur[-1]))
        return output