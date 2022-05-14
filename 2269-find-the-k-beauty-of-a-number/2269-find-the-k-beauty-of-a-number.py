class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        strnum = str(num)
        return sum([1 if int(strnum[i:i+k])!=0 and num%int(strnum[i:i+k])==0 else 0 for i in range(len(strnum)-k+1)])