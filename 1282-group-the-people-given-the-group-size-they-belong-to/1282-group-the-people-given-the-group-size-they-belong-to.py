class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        output = []
        for num in set(groupSizes):
            temp = [i for i, val in enumerate(groupSizes) if val==num]
            if len(temp)==num:
                output.append(temp)
            else:
                for start in range(0, len(temp)-num+1, num):
                    output.append(temp[start:start+num])
        return output