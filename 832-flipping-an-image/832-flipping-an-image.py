class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image = [im[::-1] for im in image]
        return [[0 if c==1 else 1 for c in row] for row in image]