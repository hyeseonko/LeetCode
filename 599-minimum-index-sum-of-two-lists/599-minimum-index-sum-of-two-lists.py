class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        output = []
        for item in set(list1)&set(list2):
            output.append((list1.index(item)+list2.index(item), item))
        soutput = sorted(output)
        result = [soutput[0][1]]
        minval = soutput[0][0]
        for val, key in soutput[1:]:
            if val==minval:
                result.append(key)
        return result