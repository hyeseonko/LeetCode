class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output = []
        for elm in arr2:
            output.extend([elm]*arr1.count(elm))
        for elm in sorted(list(set(arr1).difference(set(arr2)))):
            output.extend([elm]*arr1.count(elm))
        return output
        