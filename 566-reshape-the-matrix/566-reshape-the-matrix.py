class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c == len(mat)*len(mat[0]):
            tmp = []
            for m in mat:
                tmp.extend(m)
            output = []
            idx = 0
            for row in range(r):
                output.append(tmp[idx:idx+c])
                idx+=c
            return output
        else:
            return mat
        