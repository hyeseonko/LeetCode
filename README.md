# LeetCode
LeetCode Problems & Solutions
   
| # | Title | Solution | Topic | Basic Idea | 
|---| ----- | -------- | ------| ---------- |
|1 | [Two Sum](https://github.com/hyeseonko/LeetCode/tree/main/1-two-sum) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/1-two-sum/1-two-sum.py) | `Array`, `Hash Table` | **HashTable**: While scanning through the array, wait for the `target - x` using hash map
|15 | [3Sum](https://github.com/hyeseonko/LeetCode/tree/main/15-3sum) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/15-3sum/15-3sum.py) | `Two Pointers`, `Sorting` | 4 Cases exist: [0,0,0], [0,p,-p], [p1,p2,-(p1+p2)], [n1, n2, -(n1+n2)]
|46 | [Permutations](https://github.com/hyeseonko/LeetCode/tree/main/46-permutations) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/46-permutations/46-permutations.py) | `Backtracking` | **Backtrack**: Add nums[i] -> Go next -> Pop nums[i] with visited flag
|62 | [Unique Paths](https://github.com/hyeseonko/LeetCode/tree/main/62-unique-paths) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/62-unique-paths/62-unique-paths.py) | `Combinatorics`, `DP` | **Combinatorics**: (m+n-2)_C_(m-1), **DP**: dp[i][j]=dp[i-1][j]+dp[i][j-1] 
|77 | [Combinations](https://github.com/hyeseonko/LeetCode/tree/main/77-combinations) | [Python]() | `Backtracking` | **Backtrack**: Add i -> Go next -> Backtrack (=pop i)
|78 | [Subsets](https://github.com/hyeseonko/LeetCode/tree/main/78-subsets) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/78-subsets/78-subsets.py) | `Backtracking`, `Bit Manipulation` | **Cascading**: Append nums[i] (doubling the size of previous one) **Backtrack**: Add nums[i] -> Go next -> Backtrack (=pop nums[i])
|90 | [Subsets II](https://github.com/hyeseonko/LeetCode/tree/main/90-subsets-ii) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/90-subsets-ii/90-subsets-ii.py) | `Backtracking`, `Bit Manipulation` | **Backtrack**: Same idea as #78 + `set.add(tuple(sorted(list)))` to remove duplicates
|101 | [Symmetric Tree](https://github.com/hyeseonko/LeetCode/tree/main/101-symmetric-tree) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/101-symmetric-tree/101-symmetric-tree.py) | `DFS`, `BFS`, `Stack` | **DFS(Recursive)**: `dfs(l.l, r.r)` and `dfs(l.r, r.l)` **Stack(Iterative)**: Basically, mirror idea is SAME & return False when one is None or vals are different
|112 | [Path Sum](https://github.com/hyeseonko/LeetCode/tree/main/112-path-sum) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/112-path-sum/112-path-sum.py) | `BinarySearch`, `DFS`, `BFS` | **BFS**: (root, acc_sum)  **DFS**: (targetSum-root.val) for left and right, recursively
|221 | [Maximal Square](https://github.com/hyeseonko/LeetCode/tree/main/221-maximal-square) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/221-maximal-square/221-maximal-square.py) | `DP` | **DP**: DP[i][j]=min(DP[i][j-1], DP[i-1][j], DP[i-1][j-1])+1
|231 | [Power of Two](https://github.com/hyeseonko/LeetCode/tree/main/231-power-of-two) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/231-power-of-two/231-power-of-two.py) | `Bit Manipulation` | **BitManipulation**: (2^n) and (2^n)-1 are always complementary 
|287 | [Find the Duplicate Number](https://github.com/hyeseonko/LeetCode/tree/main/287-find-the-duplicate-number) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/287-find-the-duplicate-number/287-find-the-duplicate-number.py) | `Two Pointers`, `Binary Search`, `Bit Manipulation` | **TwoPointers**:
|322 | [Coin Change](https://github.com/hyeseonko/LeetCode/tree/main/322-coin-change) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/322-coin-change/322-coin-change.py) | `DP`, `BFS` | **DP**: dp[i]=min(dp[i-coins[0]], dp[i-coins[1]], dp[i-coins[2]], ... )+1
|518 | [Coin Change 2](https://github.com/hyeseonko/LeetCode/tree/main/518-coin-change-2) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/518-coin-change-2/518-coin-change-2.py) | `DP` | **DP**: dp[i]+=dp[i-coin] (Key idea: For-loop-coin-first-then-amount)
|1200 | [Minimum Absolute Difference](https://github.com/hyeseonko/LeetCode/tree/main/1200-minimum-absolute-difference) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/1200-minimum-absolute-difference/1200-minimum-absolute-difference.py) | `Sorting` | Sort and find the min with zip (arr, arr[1:])
|1268 | [Search Suggestions System](https://github.com/hyeseonko/LeetCode/tree/main/1268-search-suggestions-system) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/1268-search-suggestions-system/1268-search-suggestions-system.py) | `Trie`, `BinarySearch` | **BinarySearch**: sort and bisect_left **Trie**: (TBD)


Categories: Dynamic Programming (DP), BFS, DFS, Math, Stack, Queue, Hash Table, Back Tracking, Graph
## Key Point
1. Backtrack: Find **all the possible cases** for the given situation
2. DP:
3. BFS:
4. DFS:

### Reference
- [LeetHub: Linking GitHub and LeetCode](https://github.com/QasimWani/LeetHub)
 
