class Solution:
    def countLargestGroup(self, n: int) -> int:
        numarr = [0]*37 # 9999 returns the max value which is 36
        for i in range(1, n+1):
            numarr[sum([int(j) for j in str(i)])]+=1
        return numarr.count(max(numarr))
        