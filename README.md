# LeetCode
LeetCode Problems & Solutions
   
| # | Title | Solution | Topic | Basic Idea | 
|---| ----- | -------- | ------| ---------- |
|1 | [Two Sum](https://github.com/hyeseonko/LeetCode/tree/main/1-two-sum) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/1-two-sum/1-two-sum.py) | `Array`, `Hash Table` | **HashTable**: While scanning through the array, wait for the `target - x` using hash map
|46 | [Permutations](https://github.com/hyeseonko/LeetCode/tree/main/46-permutations) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/46-permutations/46-permutations.py) | `Backtracking` | **Backtrack**: Add nums[i] -> Go next -> Pop nums[i] with visited flag
|62 | [Unique Paths](https://github.com/hyeseonko/LeetCode/tree/main/62-unique-paths) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/62-unique-paths/62-unique-paths.py) | `Combinatorics`, `DP` | **Combinatorics**: (m+n-2)_C_(m-1), **DP**: dp[i][j]=dp[i-1][j]+dp[i][j-1] 
|77 | [Combinations](https://github.com/hyeseonko/LeetCode/tree/main/77-combinations) | [Python]() | `Backtracking` | **Backtrack**: Add i -> Go next -> Backtrack (=pop i)
|78 | [Subsets](https://github.com/hyeseonko/LeetCode/tree/main/78-subsets) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/78-subsets/78-subsets.py) | `Backtracking`, `Bit Manipulation` | **Cascading**: Append nums[i] (doubling the size of previous one) **Backtrack**: Add nums[i] -> Go next -> Backtrack (=pop nums[i])
|90 | [Subsets II](https://github.com/hyeseonko/LeetCode/tree/main/90-subsets-ii) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/90-subsets-ii/90-subsets-ii.py) | `Backtracking`, `Bit Manipulation` | **Backtrack**: Same idea as #78 + `set.add(tuple(sorted(list)))` to remove duplicates
|101 | [Symmetric Tree](https://github.com/hyeseonko/LeetCode/tree/main/101-symmetric-tree) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/101-symmetric-tree/101-symmetric-tree.py) | `DFS`, `BFS`, `BinaryTree` | 
|231 | [Power of Two](https://github.com/hyeseonko/LeetCode/tree/main/231-power-of-two) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/231-power-of-two/231-power-of-two.py) | `Bit Manipulation` | **BitManipulation**: (2^n) and (2^n)-1 are always complementary 


Categories: Dynamic Programming (DP), BFS, DFS, Math, Stack, Queue, Hash Table, Back Tracking, Graph
## Key Point
1. Backtrack: Find **all the possible cases** for the given situation
2. DP:
3. BFS:
4. DFS:

### Reference
- [LeetHub: Linking GitHub and LeetCode](https://github.com/QasimWani/LeetHub)
 
