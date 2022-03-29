### idea1
- item = list(nums)-set(nums)
​
### idea2
- N = len(nums)-1
- (N(N+1)/2)-sum(lens)
- Result: Wrong Answer
- counterexample: [2,2,2,2,2] (expected = 2)
​
### idea3
```
for num in nums:
if nums.count(num)!=1:
return num
```
Result: Time Limit Exceeded
​
​
### Follow up Answers
1. How can we prove that at least one duplicate number must exist in `nums`?
- can prove using Pigeon's principle.