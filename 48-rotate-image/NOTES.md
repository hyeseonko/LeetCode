### idea1
After I wrote down each roated index examples, I found a simple rule.
Let N = length of matrix row (or column)
​
1. (i, j) -> (j, N-1-i)
2. From out to in
3. Each cycle, 4 rotation exists
- (i, j) -> (j, N-1-i)
- (j, N-1-i) -> (N-1-i, N-1-j)
- (N-1-i, N-1-j) -> (N-1-j, i)
- (N-1-j, i) -> (i,j)