class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_dict = sorted([(height, i) for i, height in enumerate(heights)], reverse=True)
        return [names[v] for _, v in height_dict]
        