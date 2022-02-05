#### Logic
Build up the logic while solving examples below.
​
[0,1,0,3,2,3]
[7,7,7,7,7,7,7]
[11, 12, 13, 0, 1, 2, 3]
[11,12,13,0,1,12,13,14]
[11,12,13,0,1,14]
[10,9,2,5,3,7,10,18]
​
### idea1
```python
def getIndices(self, val) -> List[int]:
return [i for i, v in enumerate(self.dp) if v==val]
def lengthOfLIS(self, nums: List[int]) -> int:
self.dp=[1]
for num in nums[1:]:
cur_max = max(self.dp)
cur_index = self.getIndices(cur_max)[-1]
while(num<=nums[cur_index]):
cur_max -=1
if cur_max==0:
break
cur_index = self.getIndices(cur_max)[-1]
self.dp.append(cur_max+1)
return max(self.dp)
```
- Result: TLE
​
### idea2
- Let dp[i] = smallest number of last length i