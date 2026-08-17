# LeetCode

<!-- STATS:START -->
**400 problems solved** — 367 Python · 33 SQL

Easy 277 · Medium 116 · Hard 4
<!-- STATS:END -->

Solutions to LeetCode problems, one directory per problem holding the statement,
the solution, and — where a problem taught me something — a note on the idea that
cracked it.

The table below is the part worth reading: not the code, but the one-line reason
each solution works. The full index is at the bottom.

## Approach notes

| # | Title | Solution | Topic | Basic Idea | 
|---| ----- | -------- | ------| ---------- | 
|1 | [Two Sum](https://github.com/hyeseonko/LeetCode/tree/main/1-two-sum) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/1-two-sum/1-two-sum.py) | `Array`, `Hash Table` | **HashTable**: While scanning through the array, wait for the `target - x` using hash map
|15 | [3Sum](https://github.com/hyeseonko/LeetCode/tree/main/15-3sum) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/15-3sum/15-3sum.py) | `Two Pointers`, `Sorting` | 4 Cases exist: [0,0,0], [0,p,-p], [p1,p2,-(p1+p2)], [n1, n2, -(n1+n2)]
|22 | [Generate Parentheses](https://github.com/hyeseonko/LeetCode/tree/main/22-generate-parentheses) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/22-generate-parentheses/22-generate-parentheses.py) | `DP`, `Backtracking`, `Stack` | **Stack**: stack=[("(", l, r)]
|45 | [Jump Game II](https://github.com/hyeseonko/LeetCode/tree/main/45-jump-game-ii) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/45-jump-game-ii/45-jump-game-ii.py) | `DP`, `Greedy` | **DP**: O(n^2), **Greedy**: (TBD)
|46 | [Permutations](https://github.com/hyeseonko/LeetCode/tree/main/46-permutations) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/46-permutations/46-permutations.py) | `Backtracking` | **Backtrack**: Add nums[i] -> Go next -> Pop nums[i] with visited flag
|55 | [Jump Game](https://github.com/hyeseonko/LeetCode/tree/main/55-jump-game) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/55-jump-game/55-jump-game.py) | `DP`, `Greedy` | **Greedy**: (Forward) if cur position > max position then False (Backward) if last position can reach the first index then True
|62 | [Unique Paths](https://github.com/hyeseonko/LeetCode/tree/main/62-unique-paths) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/62-unique-paths/62-unique-paths.py) | `Combinatorics`, `DP` | **Combinatorics**: (m+n-2)_C_(m-1), **DP**: dp[i][j]=dp[i-1][j]+dp[i][j-1] 
|70 | [Climbing Stairs](https://github.com/hyeseonko/LeetCode/tree/main/70-climbing-stairs) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/70-climbing-stairs/70-climbing-stairs.py) | `DP`, `Math` | DP: dp[i]=dp[i-1]+dp[i-2] where dp[0]=1
|71 | [Simplify Path](https://github.com/hyeseonko/LeetCode/tree/main/71-simplify-path) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/71-simplify-path/71-simplify-path.py) | `String`, `Stack` | **Stack**: `..` (pop), `. or empty` (ignore), `else` (push) 
|77 | [Combinations](https://github.com/hyeseonko/LeetCode/tree/main/77-combinations) | [Python]() | `Backtracking` | **Backtrack**: Add i -> Go next -> Backtrack (=pop i)
|78 | [Subsets](https://github.com/hyeseonko/LeetCode/tree/main/78-subsets) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/78-subsets/78-subsets.py) | `Backtracking`, `Bit Manipulation` | **Cascading**: Append nums[i] (doubling the size of previous one) **Backtrack**: Add nums[i] -> Go next -> Backtrack (=pop nums[i])
|90 | [Subsets II](https://github.com/hyeseonko/LeetCode/tree/main/90-subsets-ii) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/90-subsets-ii/90-subsets-ii.py) | `Backtracking`, `Bit Manipulation` | **Backtrack**: Same idea as #78 + `set.add(tuple(sorted(list)))` to remove duplicates
|101 | [Symmetric Tree](https://github.com/hyeseonko/LeetCode/tree/main/101-symmetric-tree) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/101-symmetric-tree/101-symmetric-tree.py) | `DFS`, `BFS`, `Stack` | **DFS(Recursive)**: `dfs(l.l, r.r)` and `dfs(l.r, r.l)` **Stack(Iterative)**: Basically, mirror idea is SAME & return False when one is None or vals are different
|112 | [Path Sum](https://github.com/hyeseonko/LeetCode/tree/main/112-path-sum) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/112-path-sum/112-path-sum.py) | `BinarySearch`, `DFS`, `BFS` | **BFS**: (root, acc_sum)  **DFS**: (targetSum-root.val) for left and right, recursively
|113 | [Path Sum II](https://github.com/hyeseonko/LeetCode/tree/main/113-path-sum-ii) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/113-path-sum-ii/113-path-sum-ii.py) | `DFS`, `BFS`, `Backtracking` | **BFS**: (root, [root.val])
|172 | [Factorial Trailing Zeroes](https://github.com/hyeseonko/LeetCode/tree/main/172-factorial-trailing-zeroes) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/172-factorial-trailing-zeroes/172-factorial-trailing-zeroes.py) | `Math` | **O(N)**: dp[i]=i//5 + dp[i//5] if i%5==0 **O(logN)**: Add # of 5s and then # of 25s ... until it reaches N
|200 | [Number of Islands](https://github.com/hyeseonko/LeetCode/tree/main/200-number-of-islands) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/200-number-of-islands/200-number-of-islands.py) | `DFS`, `BFS`, `UnionFind` | **DFS**: dfs(x+dx, y+dy) **BFS**: queue=[(x,y)]
|221 | [Maximal Square](https://github.com/hyeseonko/LeetCode/tree/main/221-maximal-square) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/221-maximal-square/221-maximal-square.py) | `DP` | **DP**: DP[i][j]=min(DP[i][j-1], DP[i-1][j], DP[i-1][j-1])+1
|231 | [Power of Two](https://github.com/hyeseonko/LeetCode/tree/main/231-power-of-two) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/231-power-of-two/231-power-of-two.py) | `Bit Manipulation` | **BitManipulation**: (2^n) and (2^n)-1 are always complementary 
|287 | [Find the Duplicate Number](https://github.com/hyeseonko/LeetCode/tree/main/287-find-the-duplicate-number) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/287-find-the-duplicate-number/287-find-the-duplicate-number.py) | `Two Pointers`, `Binary Search`, `Bit Manipulation` | **TwoPointers**:
|322 | [Coin Change](https://github.com/hyeseonko/LeetCode/tree/main/322-coin-change) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/322-coin-change/322-coin-change.py) | `DP`, `BFS` | **DP**: dp[i]=min(dp[i-coins[0]], dp[i-coins[1]], dp[i-coins[2]], ... )+1
|326 | [Power of Three](https://github.com/hyeseonko/LeetCode/tree/main/326-power-of-three) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/326-power-of-three/326-power-of-three.py) | `Math`, `NumberTheory` | **Math**: `math.log(n, 3)`, **NumberTheory**: Check `max pow(3)%n `
|342 | [Power of Four](https://github.com/hyeseonko/LeetCode/tree/main/342-power-of-four) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/342-power-of-four/342-power-of-four.py) | `Bit Manipulation`, `Math` | **Math**: `math.log(n, 4)`
|437 | [Path Sum III](https://github.com/hyeseonko/LeetCode/tree/main/437-path-sum-iii) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/437-path-sum-iii/437-path-sum-iii.py) | `DFS`, `BFS` | (TBD)
|518 | [Coin Change 2](https://github.com/hyeseonko/LeetCode/tree/main/518-coin-change-2) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/518-coin-change-2/518-coin-change-2.py) | `DP` | **DP**: dp[i]+=dp[i-coin] (Key idea: For-loop-coin-first-then-amount)
|1051 | [Height Checker](https://github.com/hyeseonko/LeetCode/tree/main/1051-height-checker) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/1051-height-checker/1051-height-checker.py) | `Sort`, `CountingSort` | **Sort**: 1-Liner using zip & sort
|1200 | [Minimum Absolute Difference](https://github.com/hyeseonko/LeetCode/tree/main/1200-minimum-absolute-difference) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/1200-minimum-absolute-difference/1200-minimum-absolute-difference.py) | `Sorting` | Sort and find the min with zip (arr, arr[1:])
|1268 | [Search Suggestions System](https://github.com/hyeseonko/LeetCode/tree/main/1268-search-suggestions-system) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/1268-search-suggestions-system/1268-search-suggestions-system.py) | `Trie`, `BinarySearch` | **BinarySearch**: sort and bisect_left **Trie**: (TBD)
|1306 | [Jump Game III](https://github.com/hyeseonko/LeetCode/tree/main/1306-jump-game-iii) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/1306-jump-game-iii/1306-jump-game-iii.py) | `DFS`, `BFS` | **BFS**: q=[index] and A[index]=-1 **DFS**: return A[index]==0 or f(index+A[index]) or f(index-A[index])
|1512 | [Number of Good Pairs](https://github.com/hyeseonko/LeetCode/tree/main/1512-number-of-good-pairs) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/1512-number-of-good-pairs/1512-number-of-good-pairs.py) | `HashTable`, `Math`, `Counting` | **Math**: set and count (but it requires modification of the given array), **HashTable**:  Frequency Table is all you need
|2000 | [Reverse Prefix of Word](https://github.com/hyeseonko/LeetCode/tree/main/2000-reverse-prefix-of-word) | [Python](https://github.com/hyeseonko/LeetCode/blob/main/2000-reverse-prefix-of-word/2000-reverse-prefix-of-word.py) | `TwoPointers`, `String` | **String**: index and [::-1]

Recurring categories: dynamic programming, BFS, DFS, math, stack, queue, hash
table, backtracking, graph.

**Backtracking**, as a reminder to myself, is for finding *all* the possible
cases for a situation — the moment a problem says "return every", that is the
shape to reach for.

## All solutions

Generated from the repository by [`scripts/build_readme.py`](scripts/build_readme.py),
so it cannot drift from what is actually committed.

<!-- INDEX:START -->
<details>
<summary>All 400 problems</summary>

| # | Problem | Difficulty | Solution | Notes |
| --- | --- | --- | --- | --- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [Python](1-two-sum/1-two-sum.py) |  |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | [Python](2-add-two-numbers/2-add-two-numbers.py) |  |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | [Python](3-longest-substring-without-repeating-characters/3-longest-substring-without-repeating-characters.py) |  |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | [Python](4-median-of-two-sorted-arrays/4-median-of-two-sorted-arrays.py) |  |
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | [Python](5-longest-palindromic-substring/5-longest-palindromic-substring.py) |  |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Medium | [Python](reverse-integer/reverse-integer.py) |  |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | [Python](palindrome-number/palindrome-number.py) |  |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | [Python](roman-to-integer/roman-to-integer.py) |  |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | [Python](longest-common-prefix/longest-common-prefix.py) |  |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Medium | [Python](15-3sum/15-3sum.py) |  |
| 17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | [Python](17-letter-combinations-of-a-phone-number/17-letter-combinations-of-a-phone-number.py) |  |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | [Python](valid-parentheses/valid-parentheses.py) |  |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | [Python](21-merge-two-sorted-lists/21-merge-two-sorted-lists.py) |  |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | [Python](22-generate-parentheses/22-generate-parentheses.py) |  |
| 28 | [Implement strStr()](https://leetcode.com/problems/implement-strstr/) | Easy | [Python](28-implement-strstr/28-implement-strstr.py) |  |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | [Python](35-search-insert-position/35-search-insert-position.py) |  |
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | [Python](39-combination-sum/39-combination-sum.py) |  |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | [Python](42-trapping-rain-water/42-trapping-rain-water.py) |  |
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | [Python](45-jump-game-ii/45-jump-game-ii.py), [Python](jump-game-ii/jump-game-ii.py) |  |
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | Medium | [Python](46-permutations/46-permutations.py) |  |
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | [Python](48-rotate-image/48-rotate-image.py) | [notes](48-rotate-image/NOTES.md) |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | [Python](49-group-anagrams/49-group-anagrams.py) |  |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Easy | [Python](53-maximum-subarray/53-maximum-subarray.py), [Python](maximum-subarray/maximum-subarray.py) |  |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | [Python](55-jump-game/55-jump-game.py), [Python](jump-game/jump-game.py) |  |
| 58 | [Length of Last Word](https://leetcode.com/problems/length-of-last-word/) | Easy | [Python](length-of-last-word/length-of-last-word.py) |  |
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | [Python](62-unique-paths/62-unique-paths.py), [Python](unique-paths/unique-paths.py) |  |
| 63 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | Medium | [Python](63-unique-paths-ii/63-unique-paths-ii.py), [Python](unique-paths-ii/unique-paths-ii.py) |  |
| 64 | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | Medium | [Python](64-minimum-path-sum/64-minimum-path-sum.py), [Python](minimum-path-sum/minimum-path-sum.py) |  |
| 66 | [Plus One](https://leetcode.com/problems/plus-one/) | Easy | [Python](plus-one/plus-one.py) |  |
| 67 | [Add Binary](https://leetcode.com/problems/add-binary/) | Easy | [Python](67-add-binary/67-add-binary.py) |  |
| 69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy | [Python](sqrtx/sqrtx.py) |  |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | [Python](0070-climbing-stairs/0070-climbing-stairs.py), [Python](70-climbing-stairs/70-climbing-stairs.py), [Python](climbing-stairs/climbing-stairs.py) |  |
| 71 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | Medium | [Python](71-simplify-path/71-simplify-path.py) |  |
| 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | [Python](73-set-matrix-zeroes/73-set-matrix-zeroes.py) |  |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | [Python](75-sort-colors/75-sort-colors.py) |  |
| 77 | [Combinations](https://leetcode.com/problems/combinations/) | Medium | [Python](77-combinations/77-combinations.py) |  |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | Medium | [Python](78-subsets/78-subsets.py) |  |
| 81 | [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | Medium | [Python](81-search-in-rotated-sorted-array-ii/81-search-in-rotated-sorted-array-ii.py) |  |
| 83 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Easy | [Python](83-remove-duplicates-from-sorted-list/83-remove-duplicates-from-sorted-list.py) |  |
| 86 | [Partition List](https://leetcode.com/problems/partition-list/) | Medium | [Python](86-partition-list/86-partition-list.py) |  |
| 90 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | Medium | [Python](90-subsets-ii/90-subsets-ii.py) |  |
| 91 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium | [Python](91-decode-ways/91-decode-ways.py) |  |
| 96 | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | Medium | [Python](0096-unique-binary-search-trees/0096-unique-binary-search-trees.py), [Python](96-unique-binary-search-trees/96-unique-binary-search-trees.py) |  |
| 100 | [Same Tree](https://leetcode.com/problems/same-tree/) | Easy | [Python](same-tree/same-tree.py) |  |
| 101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | Easy | [Python](101-symmetric-tree/101-symmetric-tree.py) |  |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | [Python](102-binary-tree-level-order-traversal/102-binary-tree-level-order-traversal.py), [Python](binary-tree-level-order-traversal/binary-tree-level-order-traversal.py) |  |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | [Python](104-maximum-depth-of-binary-tree/104-maximum-depth-of-binary-tree.py), [Python](maximum-depth-of-binary-tree/maximum-depth-of-binary-tree.py) |  |
| 108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Easy | [Python](108-convert-sorted-array-to-binary-search-tree/108-convert-sorted-array-to-binary-search-tree.py) |  |
| 109 | [Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) | Medium | [Python](109-convert-sorted-list-to-binary-search-tree/109-convert-sorted-list-to-binary-search-tree.py) |  |
| 111 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | Easy | [Python](minimum-depth-of-binary-tree/minimum-depth-of-binary-tree.py) |  |
| 112 | [Path Sum](https://leetcode.com/problems/path-sum/) | Easy | [Python](112-path-sum/112-path-sum.py) |  |
| 113 | [Path Sum II](https://leetcode.com/problems/path-sum-ii/) | Medium | [Python](113-path-sum-ii/113-path-sum-ii.py) |  |
| 118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | Easy | [Python](0118-pascals-triangle/0118-pascals-triangle.py), [Python](118-pascals-triangle/118-pascals-triangle.py), [Python](pascals-triangle/pascals-triangle.py) |  |
| 119 | [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) | Easy | [Python](0119-pascals-triangle-ii/0119-pascals-triangle-ii.py), [Python](119-pascals-triangle-ii/119-pascals-triangle-ii.py), [Python](pascals-triangle-ii/pascals-triangle-ii.py) |  |
| 120 | [Triangle](https://leetcode.com/problems/triangle/) | Medium | [Python](0120-triangle/0120-triangle.py), [Python](120-triangle/120-triangle.py), [Python](triangle/triangle.py) |  |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | [Python](121-best-time-to-buy-and-sell-stock/121-best-time-to-buy-and-sell-stock.py), [Python](best-time-to-buy-and-sell-stock/best-time-to-buy-and-sell-stock.py) |  |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Medium | [Python](122-best-time-to-buy-and-sell-stock-ii/122-best-time-to-buy-and-sell-stock-ii.py) |  |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | [Python](125-valid-palindrome/125-valid-palindrome.py) |  |
| 129 | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | Medium | [Python](129-sum-root-to-leaf-numbers/129-sum-root-to-leaf-numbers.py) |  |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | [Python](single-number/single-number.py) |  |
| 137 | [Single Number II](https://leetcode.com/problems/single-number-ii/) | Medium | [Python](137-single-number-ii/137-single-number-ii.py) |  |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium | [Python](0152-maximum-product-subarray/0152-maximum-product-subarray.py), [Python](152-maximum-product-subarray/152-maximum-product-subarray.py), [Python](maximum-product-subarray/maximum-product-subarray.py) |  |
| 162 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium | [Python](162-find-peak-element/162-find-peak-element.py) |  |
| 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Easy | [Python](two-sum-ii-input-array-is-sorted/two-sum-ii-input-array-is-sorted.py) |  |
| 169 | [Majority Element](https://leetcode.com/problems/majority-element/) | Easy | [Python](169-majority-element/169-majority-element.py) |  |
| 171 | [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/) | Easy | [Python](excel-sheet-column-number/excel-sheet-column-number.py) |  |
| 172 | [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) | Medium | [Python](172-factorial-trailing-zeroes/172-factorial-trailing-zeroes.py) |  |
| 175 | [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) | Easy | [SQL](175-combine-two-tables/175-combine-two-tables.sql) |  |
| 176 | [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) | Medium | [SQL](176-second-highest-salary/176-second-highest-salary.sql) |  |
| 182 | [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) | Easy | [SQL](182-duplicate-emails/182-duplicate-emails.sql) |  |
| 183 | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) | Easy | [SQL](183-customers-who-never-order/183-customers-who-never-order.sql) |  |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) | Medium | [Python](rotate-array/rotate-array.py) |  |
| 191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | [Python](191-number-of-1-bits/191-number-of-1-bits.py) |  |
| 196 | [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/) | Easy | [SQL](196-delete-duplicate-emails/196-delete-duplicate-emails.sql) |  |
| 197 | [Rising Temperature](https://leetcode.com/problems/rising-temperature/) | Easy | [SQL](197-rising-temperature/197-rising-temperature.sql) |  |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | Medium | [Python](198-house-robber/198-house-robber.py), [Python](house-robber/house-robber.py) |  |
| 199 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | [Python](199-binary-tree-right-side-view/199-binary-tree-right-side-view.py), [Python](binary-tree-right-side-view/binary-tree-right-side-view.py) |  |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | [Python](200-number-of-islands/200-number-of-islands.py), [Python](number-of-islands/number-of-islands.py) |  |
| 202 | [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | [Python](202-happy-number/202-happy-number.py) |  |
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) | Easy | [Python](203-remove-linked-list-elements/203-remove-linked-list-elements.py) |  |
| 204 | [Count Primes](https://leetcode.com/problems/count-primes/) | Medium | [Python](count-primes/count-primes.py) |  |
| 205 | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | Easy | [Python](205-isomorphic-strings/205-isomorphic-strings.py) |  |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | [Python](206-reverse-linked-list/206-reverse-linked-list.py) |  |
| 213 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Medium | [Python](213-house-robber-ii/213-house-robber-ii.py), [Python](house-robber-ii/house-robber-ii.py) |  |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | [Python](215-kth-largest-element-in-an-array/215-kth-largest-element-in-an-array.py) |  |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | [Python](217-contains-duplicate/217-contains-duplicate.py), [Python](contains-duplicate/contains-duplicate.py) |  |
| 221 | [Maximal Square](https://leetcode.com/problems/maximal-square/) | Medium | [Python](221-maximal-square/221-maximal-square.py), [Python](maximal-square/maximal-square.py) |  |
| 225 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | Easy | [Python](225-implement-stack-using-queues/225-implement-stack-using-queues.py) |  |
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | [Python](226-invert-binary-tree/226-invert-binary-tree.py) |  |
| 228 | [Summary Ranges](https://leetcode.com/problems/summary-ranges/) | Easy | [Python](228-summary-ranges/228-summary-ranges.py) |  |
| 230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | [Python](230-kth-smallest-element-in-a-bst/230-kth-smallest-element-in-a-bst.py) |  |
| 231 | [Power of Two](https://leetcode.com/problems/power-of-two/) | Easy | [Python](231-power-of-two/231-power-of-two.py), [Python](power-of-two/power-of-two.py) |  |
| 232 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Easy | [Python](232-implement-queue-using-stacks/232-implement-queue-using-stacks.py) |  |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Easy | [Python](234-palindrome-linked-list/234-palindrome-linked-list.py) |  |
| 237 | [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) | Easy | [Python](237-delete-node-in-a-linked-list/237-delete-node-in-a-linked-list.py) |  |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | [Python](238-product-of-array-except-self/238-product-of-array-except-self.py) |  |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | [Python](242-valid-anagram/242-valid-anagram.py) |  |
| 258 | [Add Digits](https://leetcode.com/problems/add-digits/) | Easy | [Python](258-add-digits/258-add-digits.py), [Python](add-digits/add-digits.py) |  |
| 263 | [Ugly Number](https://leetcode.com/problems/ugly-number/) | Easy | [Python](ugly-number/ugly-number.py) |  |
| 268 | [Missing Number](https://leetcode.com/problems/missing-number/) | Easy | [Python](268-missing-number/268-missing-number.py), [Python](missing-number/missing-number.py) |  |
| 279 | [Perfect Squares](https://leetcode.com/problems/perfect-squares/) | Medium | [Python](perfect-squares/perfect-squares.py) |  |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | [Python](283-move-zeroes/283-move-zeroes.py), [Python](move-zeroes/move-zeroes.py) |  |
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | [Python](287-find-the-duplicate-number/287-find-the-duplicate-number.py) |  |
| 290 | [Word Pattern](https://leetcode.com/problems/word-pattern/) | Easy | [Python](290-word-pattern/290-word-pattern.py) | [notes](290-word-pattern/NOTES.md) |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | [Python](300-longest-increasing-subsequence/300-longest-increasing-subsequence.py) |  |
| 303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | [Python](303-range-sum-query-immutable/303-range-sum-query-immutable.py) |  |
| 318 | [Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/) | Medium | [Python](318-maximum-product-of-word-lengths/318-maximum-product-of-word-lengths.py) |  |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | Medium | [Python](322-coin-change/322-coin-change.py), [Python](coin-change/coin-change.py) |  |
| 326 | [Power of Three](https://leetcode.com/problems/power-of-three/) | Easy | [Python](326-power-of-three/326-power-of-three.py), [Python](power-of-three/power-of-three.py) |  |
| 328 | [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) | Medium | [Python](328-odd-even-linked-list/328-odd-even-linked-list.py) |  |
| 329 | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | Hard | [Python](329-longest-increasing-path-in-a-matrix/329-longest-increasing-path-in-a-matrix.py) |  |
| 334 | [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | Medium | [Python](334-increasing-triplet-subsequence/334-increasing-triplet-subsequence.py) |  |
| 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | [Python](338-counting-bits/338-counting-bits.py) |  |
| 342 | [Power of Four](https://leetcode.com/problems/power-of-four/) | Easy | [Python](342-power-of-four/342-power-of-four.py), [Python](power-of-four/power-of-four.py) |  |
| 343 | [Integer Break](https://leetcode.com/problems/integer-break/) | Medium | [Python](343-integer-break/343-integer-break.py) |  |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | [Python](reverse-string/reverse-string.py) |  |
| 345 | [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) | Easy | [Python](345-reverse-vowels-of-a-string/345-reverse-vowels-of-a-string.py) |  |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | [Python](347-top-k-frequent-elements/347-top-k-frequent-elements.py) |  |
| 349 | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | Easy | [Python](intersection-of-two-arrays/intersection-of-two-arrays.py) |  |
| 367 | [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) | Easy | [Python](367-valid-perfect-square/367-valid-perfect-square.py) |  |
| 371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | [Python](371-sum-of-two-integers/371-sum-of-two-integers.py) |  |
| 374 | [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/solution/) | Easy | [Python](374-guess-number-higher-or-lower/374-guess-number-higher-or-lower.py) |  |
| 377 | [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) | Medium | [Python](377-combination-sum-iv/377-combination-sum-iv.py) |  |
| 378 | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Medium | [Python](378-kth-smallest-element-in-a-sorted-matrix/378-kth-smallest-element-in-a-sorted-matrix.py) |  |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | Easy | [Python](387-first-unique-character-in-a-string/387-first-unique-character-in-a-string.py) |  |
| 389 | [Find the Difference](https://leetcode.com/problems/find-the-difference/) | Easy | [Python](389-find-the-difference/389-find-the-difference.py), [Python](find-the-difference/find-the-difference.py) |  |
| 392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Easy | [Python](392-is-subsequence/392-is-subsequence.py), [Python](is-subsequence/is-subsequence.py) |  |
| 404 | [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) | Easy | [Python](404-sum-of-left-leaves/404-sum-of-left-leaves.py), [Python](sum-of-left-leaves/sum-of-left-leaves.py) |  |
| 409 | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | Easy | [Python](longest-palindrome/longest-palindrome.py) |  |
| 412 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Easy | [Python](412-fizz-buzz/412-fizz-buzz.py) |  |
| 413 | [Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices/) | Medium | [Python](413-arithmetic-slices/413-arithmetic-slices.py) |  |
| 414 | [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) | Easy | [Python](414-third-maximum-number/414-third-maximum-number.py) |  |
| 415 | [Add Strings](https://leetcode.com/problems/add-strings/) | Easy | [Python](415-add-strings/415-add-strings.py) |  |
| 434 | [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/) | Easy | [Python](434-number-of-segments-in-a-string/434-number-of-segments-in-a-string.py) |  |
| 437 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | Medium | [Python](437-path-sum-iii/437-path-sum-iii.py) |  |
| 441 | [Arranging Coins](https://leetcode.com/problems/arranging-coins/) | Easy | [Python](441-arranging-coins/441-arranging-coins.py) |  |
| 451 | [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | Medium | [Python](451-sort-characters-by-frequency/451-sort-characters-by-frequency.py) |  |
| 459 | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | Easy | [Python](459-repeated-substring-pattern/459-repeated-substring-pattern.py) |  |
| 461 | [Hamming Distance](https://leetcode.com/problems/hamming-distance/) | Easy | [Python](461-hamming-distance/461-hamming-distance.py) |  |
| 476 | [Number Complement](https://leetcode.com/problems/number-complement/) | Easy | [Python](0476-number-complement/0476-number-complement.py) |  |
| 496 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Easy | [Python](496-next-greater-element-i/496-next-greater-element-i.py) |  |
| 500 | [Keyboard Row](https://leetcode.com/problems/keyboard-row/) | Easy | [Python](500-keyboard-row/500-keyboard-row.py) |  |
| 504 | [Base 7](https://leetcode.com/problems/base-7/) | Easy | [Python](504-base-7/504-base-7.py) |  |
| 509 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Easy | [Python](509-fibonacci-number/509-fibonacci-number.py), [Python](fibonacci-number/fibonacci-number.py) |  |
| 511 | [Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) | Easy | [SQL](511-game-play-analysis-i/511-game-play-analysis-i.sql) |  |
| 513 | [Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value/) | Medium | [Python](find-bottom-left-tree-value/find-bottom-left-tree-value.py) |  |
| 515 | [Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/) | Medium | [Python](515-find-largest-value-in-each-tree-row/515-find-largest-value-in-each-tree-row.py) |  |
| 516 | [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) | Medium | [Python](516-longest-palindromic-subsequence/516-longest-palindromic-subsequence.py) |  |
| 518 | [Coin Change 2](https://leetcode.com/problems/coin-change-2/) | Medium | [Python](518-coin-change-2/518-coin-change-2.py), [Python](518-coin-change-ii/518-coin-change-ii.py) |  |
| 520 | [Detect Capital](https://leetcode.com/problems/detect-capital/) | Easy | [Python](520-detect-capital/520-detect-capital.py) |  |
| 530 | [Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/) | Easy | [Python](minimum-absolute-difference-in-bst/minimum-absolute-difference-in-bst.py) |  |
| 535 | [Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/) | Medium | [Python](535-encode-and-decode-tinyurl/535-encode-and-decode-tinyurl.py) | [notes](535-encode-and-decode-tinyurl/NOTES.md) |
| 537 | [Complex Number Multiplication](https://leetcode.com/problems/complex-number-multiplication/) | Medium | [Python](537-complex-number-multiplication/537-complex-number-multiplication.py) |  |
| 539 | [Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference/) | Medium | [Python](539-minimum-time-difference/539-minimum-time-difference.py) |  |
| 547 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | [Python](number-of-provinces/number-of-provinces.py) |  |
| 557 | [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) | Easy | [Python](557-reverse-words-in-a-string-iii/557-reverse-words-in-a-string-iii.py) |  |
| 559 | [Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) | Easy | [Python](559-maximum-depth-of-n-ary-tree/559-maximum-depth-of-n-ary-tree.py) |  |
| 561 | [Array Partition I](https://leetcode.com/problems/array-partition-i/) | Easy | [Python](561-array-partition-i/561-array-partition-i.py) |  |
| 566 | [Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/) | Easy | [Python](566-reshape-the-matrix/566-reshape-the-matrix.py) |  |
| 583 | [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) | Medium | [Python](583-delete-operation-for-two-strings/583-delete-operation-for-two-strings.py) |  |
| 584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | Easy | [SQL](584-find-customer-referee/584-find-customer-referee.sql) |  |
| 589 | [N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) | Easy | [Python](589-n-ary-tree-preorder-traversal/589-n-ary-tree-preorder-traversal.py) |  |
| 594 | [Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/) | Easy | [Python](594-longest-harmonious-subsequence/594-longest-harmonious-subsequence.py) |  |
| 595 | [Big Countries](https://leetcode.com/problems/big-countries/) | Easy | [SQL](595-big-countries/595-big-countries.sql) |  |
| 599 | [Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists/) | Easy | [Python](599-minimum-index-sum-of-two-lists/599-minimum-index-sum-of-two-lists.py) |  |
| 607 | [Sales Person](https://leetcode.com/problems/sales-person/) | Easy | [SQL](607-sales-person/607-sales-person.sql) |  |
| 608 | [Tree Node](https://leetcode.com/problems/tree-node/) | Medium | [SQL](608-tree-node/608-tree-node.sql) |  |
| 620 | [Not Boring Movies](https://leetcode.com/problems/not-boring-movies/) | Easy | [SQL](620-not-boring-movies/620-not-boring-movies.sql) |  |
| 627 | [Swap Salary](https://leetcode.com/problems/swap-salary/) | Easy | [SQL](627-swap-salary/627-swap-salary.sql) |  |
| 637 | [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/) | Easy | [Python](average-of-levels-in-binary-tree/average-of-levels-in-binary-tree.py) |  |
| 653 | [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) | Easy | [Python](653-two-sum-iv-input-is-a-bst/653-two-sum-iv-input-is-a-bst.py) |  |
| 657 | [Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/) | Easy | [Python](657-robot-return-to-origin/657-robot-return-to-origin.py) |  |
| 682 | [Baseball Game](https://leetcode.com/problems/baseball-game/) | Easy | [Python](682-baseball-game/682-baseball-game.py) |  |
| 695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | [Python](695-max-area-of-island/695-max-area-of-island.py), [Python](max-area-of-island/max-area-of-island.py) |  |
| 697 | [Degree of an Array](https://leetcode.com/problems/degree-of-an-array/) | Easy | [Python](697-degree-of-an-array/697-degree-of-an-array.py) |  |
| 700 | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Easy | [Python](700-search-in-a-binary-search-tree/700-search-in-a-binary-search-tree.py) |  |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | [Python](704-binary-search/704-binary-search.py), [Python](binary-search/binary-search.py) |  |
| 709 | [To Lower Case](https://leetcode.com/problems/to-lower-case/) | Easy | [Python](709-to-lower-case/709-to-lower-case.py) |  |
| 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Easy | [Python](724-find-pivot-index/724-find-pivot-index.py) |  |
| 728 | [Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/) | Easy | [Python](728-self-dividing-numbers/728-self-dividing-numbers.py) |  |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | [Python](739-daily-temperatures/739-daily-temperatures.py) |  |
| 746 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | Easy | [Python](746-min-cost-climbing-stairs/746-min-cost-climbing-stairs.py), [Python](min-cost-climbing-stairs/min-cost-climbing-stairs.py) |  |
| 766 | [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/) | Easy | [Python](766-toeplitz-matrix/766-toeplitz-matrix.py) |  |
| 771 | [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) | Easy | [Python](771-jewels-and-stones/771-jewels-and-stones.py) |  |
| 783 | [Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/) | Easy | [Python](783-minimum-distance-between-bst-nodes/783-minimum-distance-between-bst-nodes.py) |  |
| 796 | [Rotate String](https://leetcode.com/problems/rotate-string/) | Easy | [Python](796-rotate-string/796-rotate-string.py) |  |
| 804 | [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/) | Easy | [Python](804-unique-morse-code-words/804-unique-morse-code-words.py) |  |
| 832 | [Flipping an Image](https://leetcode.com/problems/flipping-an-image/) | Easy | [Python](832-flipping-an-image/832-flipping-an-image.py) |  |
| 844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | Easy | [Python](844-backspace-string-compare/844-backspace-string-compare.py) |  |
| 852 | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) | Easy | [Python](852-peak-index-in-a-mountain-array/852-peak-index-in-a-mountain-array.py) |  |
| 856 | [Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/) | Medium | [Python](856-score-of-parentheses/856-score-of-parentheses.py) |  |
| 867 | [Transpose Matrix](https://leetcode.com/problems/transpose-matrix/) | Easy | [Python](867-transpose-matrix/867-transpose-matrix.py) |  |
| 868 | [Binary Gap](https://leetcode.com/problems/binary-gap/) | Easy | [Python](868-binary-gap/868-binary-gap.py) |  |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | [Python](876-middle-of-the-linked-list/876-middle-of-the-linked-list.py) |  |
| 884 | [Uncommon Words from Two Sentences](https://leetcode.com/problems/uncommon-words-from-two-sentences/) | Easy | [Python](884-uncommon-words-from-two-sentences/884-uncommon-words-from-two-sentences.py) |  |
| 890 | [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/) | Medium | [Python](890-find-and-replace-pattern/890-find-and-replace-pattern.py) |  |
| 905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) | Easy | [Python](905-sort-array-by-parity/905-sort-array-by-parity.py) |  |
| 908 | [Smallest Range I](https://leetcode.com/problems/smallest-range-i/) | Easy | [Python](908-smallest-range-i/908-smallest-range-i.py) |  |
| 916 | [Word Subsets](https://leetcode.com/problems/word-subsets/) | Medium | [Python](916-word-subsets/916-word-subsets.py) |  |
| 922 | [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/) | Easy | [Python](922-sort-array-by-parity-ii/922-sort-array-by-parity-ii.py) |  |
| 931 | [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) | Medium | [Python](0931-minimum-falling-path-sum/0931-minimum-falling-path-sum.py), [Python](931-minimum-falling-path-sum/931-minimum-falling-path-sum.py) |  |
| 938 | [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/) | Easy | [Python](938-range-sum-of-bst/938-range-sum-of-bst.py) |  |
| 942 | [DI String Match](https://leetcode.com/problems/di-string-match/) | Easy | [Python](942-di-string-match/942-di-string-match.py) |  |
| 953 | [Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/) | Easy | [Python](953-verifying-an-alien-dictionary/953-verifying-an-alien-dictionary.py) |  |
| 961 | [N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/) | Easy | [Python](961-n-repeated-element-in-size-2n-array/961-n-repeated-element-in-size-2n-array.py) |  |
| 965 | [Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/) | Easy | [Python](965-univalued-binary-tree/965-univalued-binary-tree.py) |  |
| 976 | [Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/) | Easy | [Python](0976-largest-perimeter-triangle/0976-largest-perimeter-triangle.py), [Python](976-largest-perimeter-triangle/976-largest-perimeter-triangle.py) |  |
| 977 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | Easy | [Python](squares-of-a-sorted-array/squares-of-a-sorted-array.py) |  |
| 983 | [Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/) | Medium | [Python](983-minimum-cost-for-tickets/983-minimum-cost-for-tickets.py) |  |
| 988 | [Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf/) | Medium | [Python](988-smallest-string-starting-from-leaf/988-smallest-string-starting-from-leaf.py) |  |
| 993 | [Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/) | Easy | [Python](cousins-in-binary-tree/cousins-in-binary-tree.py) |  |
| 1002 | [Find Common Characters](https://leetcode.com/problems/find-common-characters/) | Easy | [Python](find-common-characters/find-common-characters.py) |  |
| 1009 | [Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/) | Easy | [Python](1009-complement-of-base-10-integer/1009-complement-of-base-10-integer.py) |  |
| 1014 | [Best Sightseeing Pair](https://leetcode.com/problems/best-sightseeing-pair/) | Medium | [Python](1014-best-sightseeing-pair/1014-best-sightseeing-pair.py) |  |
| 1018 | [Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/) | Easy | [Python](1018-binary-prefix-divisible-by-5/1018-binary-prefix-divisible-by-5.py) |  |
| 1021 | [Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/) | Easy | [Python](1021-remove-outermost-parentheses/1021-remove-outermost-parentheses.py) |  |
| 1022 | [Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/) | Easy | [Python](1022-sum-of-root-to-leaf-binary-numbers/1022-sum-of-root-to-leaf-binary-numbers.py) |  |
| 1029 | [Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/) | Medium | [Python](1029-two-city-scheduling/1029-two-city-scheduling.py) | [notes](1029-two-city-scheduling/NOTES.md) |
| 1043 | [Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/) | Medium | [Python](1043-partition-array-for-maximum-sum/1043-partition-array-for-maximum-sum.py) |  |
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy | [Python](1046-last-stone-weight/1046-last-stone-weight.py) |  |
| 1050 | [Actors and Directors Who Cooperated At Least Three Times](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/) | Easy | [SQL](1050-actors-and-directors-who-cooperated-at-least-three-times/1050-actors-and-directors-who-cooperated-at-least-three-times.sql) |  |
| 1051 | [Height Checker](https://leetcode.com/problems/height-checker/) | Easy | [Python](1051-height-checker/1051-height-checker.py) |  |
| 1084 | [Sales Analysis III](https://leetcode.com/problems/sales-analysis-iii/) | Easy | [SQL](1084-sales-analysis-iii/1084-sales-analysis-iii.sql) |  |
| 1091 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium | [Python](1091-shortest-path-in-binary-matrix/1091-shortest-path-in-binary-matrix.py) |  |
| 1108 | [Defanging an IP Address](https://leetcode.com/problems/defanging-an-ip-address/) | Easy | [Python](1108-defanging-an-ip-address/1108-defanging-an-ip-address.py) |  |
| 1122 | [Relative Sort Array](https://leetcode.com/problems/relative-sort-array/) | Easy | [Python](1122-relative-sort-array/1122-relative-sort-array.py) | [notes](1122-relative-sort-array/NOTES.md) |
| 1137 | [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) | Easy | [Python](1137-n-th-tribonacci-number/1137-n-th-tribonacci-number.py), [Python](n-th-tribonacci-number/n-th-tribonacci-number.py) |  |
| 1141 | [User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) | Easy | [SQL](1141-user-activity-for-the-past-30-days-i/1141-user-activity-for-the-past-30-days-i.sql) |  |
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | [Python](1143-longest-common-subsequence/1143-longest-common-subsequence.py) |  |
| 1148 | [Article Views I](https://leetcode.com/problems/article-views-i/) | Easy | [SQL](1148-article-views-i/1148-article-views-i.sql) |  |
| 1158 | [Market Analysis I](https://leetcode.com/problems/market-analysis-i/) | Medium | [SQL](1158-market-analysis-i/1158-market-analysis-i.sql) |  |
| 1160 | [Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/) | Easy | [Python](1160-find-words-that-can-be-formed-by-characters/1160-find-words-that-can-be-formed-by-characters.py) |  |
| 1161 | [Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) | Medium | [Python](1161-maximum-level-sum-of-a-binary-tree/1161-maximum-level-sum-of-a-binary-tree.py) |  |
| 1200 | [Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/) | Easy | [Python](1200-minimum-absolute-difference/1200-minimum-absolute-difference.py) |  |
| 1207 | [Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/) | Easy | [Python](1207-unique-number-of-occurrences/1207-unique-number-of-occurrences.py) |  |
| 1221 | [Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/) | Easy | [Python](1221-split-a-string-in-balanced-strings/1221-split-a-string-in-balanced-strings.py) |  |
| 1232 | [Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/) | Easy | [Python](1232-check-if-it-is-a-straight-line/1232-check-if-it-is-a-straight-line.py) |  |
| 1252 | [Cells with Odd Values in a Matrix](https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/) | Easy | [Python](1252-cells-with-odd-values-in-a-matrix/1252-cells-with-odd-values-in-a-matrix.py) |  |
| 1254 | [Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) | Medium | [Python](1254-number-of-closed-islands/1254-number-of-closed-islands.py) |  |
| 1266 | [Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/) | Easy | [Python](1266-minimum-time-visiting-all-points/1266-minimum-time-visiting-all-points.py) |  |
| 1268 | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Medium | [Python](1268-search-suggestions-system/1268-search-suggestions-system.py) |  |
| 1277 | [Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) | Medium | [Python](1277-count-square-submatrices-with-all-ones/1277-count-square-submatrices-with-all-ones.py) |  |
| 1281 | [Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) | Easy | [Python](1281-subtract-the-product-and-sum-of-digits-of-an-integer/1281-subtract-the-product-and-sum-of-digits-of-an-integer.py) |  |
| 1282 | [Group the People Given the Group Size They Belong To](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/) | Medium | [Python](1282-group-the-people-given-the-group-size-they-belong-to/1282-group-the-people-given-the-group-size-they-belong-to.py) |  |
| 1290 | [Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) | Easy | [Python](1290-convert-binary-number-in-a-linked-list-to-integer/1290-convert-binary-number-in-a-linked-list-to-integer.py) |  |
| 1295 | [Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) | Easy | [Python](1295-find-numbers-with-even-number-of-digits/1295-find-numbers-with-even-number-of-digits.py) |  |
| 1299 | [Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) | Easy | [Python](1299-replace-elements-with-greatest-element-on-right-side/1299-replace-elements-with-greatest-element-on-right-side.py) |  |
| 1302 | [Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/) | Medium | [Python](1302-deepest-leaves-sum/1302-deepest-leaves-sum.py) |  |
| 1304 | [Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/) | Easy | [Python](1304-find-n-unique-integers-sum-up-to-zero/1304-find-n-unique-integers-sum-up-to-zero.py) | [notes](1304-find-n-unique-integers-sum-up-to-zero/NOTES.md) |
| 1306 | [Jump Game III](https://leetcode.com/problems/jump-game-iii/) | Medium | [Python](1306-jump-game-iii/1306-jump-game-iii.py), [Python](jump-game-iii/jump-game-iii.py) |  |
| 1309 | [Decrypt String from Alphabet to Integer Mapping](https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/) | Easy | [Python](1309-decrypt-string-from-alphabet-to-integer-mapping/1309-decrypt-string-from-alphabet-to-integer-mapping.py) |  |
| 1313 | [Decompress Run-Length Encoded List](https://leetcode.com/problems/decompress-run-length-encoded-list/) | Easy | [Python](1313-decompress-run-length-encoded-list/1313-decompress-run-length-encoded-list.py) |  |
| 1323 | [Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/) | Easy | [Python](1323-maximum-69-number/1323-maximum-69-number.py) |  |
| 1337 | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) | Easy | [Python](1337-the-k-weakest-rows-in-a-matrix/1337-the-k-weakest-rows-in-a-matrix.py) | [notes](1337-the-k-weakest-rows-in-a-matrix/NOTES.md) |
| 1342 | [Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) | Easy | [Python](1342-number-of-steps-to-reduce-a-number-to-zero/1342-number-of-steps-to-reduce-a-number-to-zero.py) |  |
| 1351 | [Count Negative Numbers In A Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) | — | [Python](1351-count-negative-numbers-in-a-sorted-matrix/1351-count-negative-numbers-in-a-sorted-matrix.py) |  |
| 1356 | [Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) | Easy | [Python](1356-sort-integers-by-the-number-of-1-bits/1356-sort-integers-by-the-number-of-1-bits.py) |  |
| 1365 | [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | Easy | [Python](1365-how-many-numbers-are-smaller-than-the-current-number/1365-how-many-numbers-are-smaller-than-the-current-number.py) |  |
| 1374 | [Generate a String With Characters That Have Odd Counts](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/) | Easy | [Python](1374-generate-a-string-with-characters-that-have-odd-counts/1374-generate-a-string-with-characters-that-have-odd-counts.py) |  |
| 1380 | [Lucky Numbers in a Matrix](https://leetcode.com/problems/lucky-numbers-in-a-matrix/) | Easy | [Python](1380-lucky-numbers-in-a-matrix/1380-lucky-numbers-in-a-matrix.py) |  |
| 1385 | [Find the Distance Value Between Two Arrays](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/) | Easy | [Python](1385-find-the-distance-value-between-two-arrays/1385-find-the-distance-value-between-two-arrays.py) |  |
| 1389 | [Create Target Array in the Given Order](https://leetcode.com/problems/create-target-array-in-the-given-order/) | Easy | [Python](1389-create-target-array-in-the-given-order/1389-create-target-array-in-the-given-order.py) |  |
| 1393 | [Capital Gain/Loss](https://leetcode.com/problems/capital-gainloss/) | Medium | [SQL](1393-capital-gain-loss/1393-capital-gain-loss.sql) |  |
| 1399 | [Count Largest Group](https://leetcode.com/problems/count-largest-group/) | Easy | [Python](1399-count-largest-group/1399-count-largest-group.py) |  |
| 1407 | [Top Travellers](https://leetcode.com/problems/top-travellers/) | Easy | [SQL](1407-top-travellers/1407-top-travellers.sql) |  |
| 1431 | [Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) | Easy | [Python](1431-kids-with-the-greatest-number-of-candies/1431-kids-with-the-greatest-number-of-candies.py) |  |
| 1436 | [Destination City](https://leetcode.com/problems/destination-city/) | Easy | [Python](1436-destination-city/1436-destination-city.py) |  |
| 1441 | [Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/) | Easy | [Python](1441-build-an-array-with-stack-operations/1441-build-an-array-with-stack-operations.py) |  |
| 1446 | [Consecutive Characters](https://leetcode.com/problems/consecutive-characters/) | Easy | [Python](1446-consecutive-characters/1446-consecutive-characters.py) |  |
| 1448 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Medium | [Python](1448-count-good-nodes-in-binary-tree/1448-count-good-nodes-in-binary-tree.py) |  |
| 1450 | [Number of Students Doing Homework at a Given Time](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/) | Easy | [Python](1450-number-of-students-doing-homework-at-a-given-time/1450-number-of-students-doing-homework-at-a-given-time.py) |  |
| 1455 | [Check If a Word Occurs As a Prefix of Any Word in a Sentence](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/) | Easy | [Python](1455-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/1455-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence.py) |  |
| 1461 | [Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) | Medium | [Python](1461-check-if-a-string-contains-all-binary-codes-of-size-k/1461-check-if-a-string-contains-all-binary-codes-of-size-k.py) |  |
| 1464 | [Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) | Easy | [Python](1464-maximum-product-of-two-elements-in-an-array/1464-maximum-product-of-two-elements-in-an-array.py) |  |
| 1470 | [Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/) | Easy | [Python](1470-shuffle-the-array/1470-shuffle-the-array.py) |  |
| 1475 | [Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) | Easy | [Python](1475-final-prices-with-a-special-discount-in-a-shop/1475-final-prices-with-a-special-discount-in-a-shop.py) |  |
| 1480 | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Easy | [Python](1480-running-sum-of-1d-array/1480-running-sum-of-1d-array.py) |  |
| 1484 | [Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/) | Easy | [SQL](1484-group-sold-products-by-the-date/1484-group-sold-products-by-the-date.sql) |  |
| 1491 | [Average Salary Excluding the Minimum and Maximum Salary](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/) | Easy | [Python](1491-average-salary-excluding-the-minimum-and-maximum-salary/1491-average-salary-excluding-the-minimum-and-maximum-salary.py) |  |
| 1502 | [Can Make Arithmetic Progression From Sequence](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/) | Easy | [Python](1502-can-make-arithmetic-progression-from-sequence/1502-can-make-arithmetic-progression-from-sequence.py) |  |
| 1509 | [Minimum Difference Between Largest and Smallest Value in Three Moves](https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/) | Medium | [Python](1509-minimum-difference-between-largest-and-smallest-value-in-three-moves/1509-minimum-difference-between-largest-and-smallest-value-in-three-moves.py) |  |
| 1512 | [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) | Easy | [Python](1512-number-of-good-pairs/1512-number-of-good-pairs.py) |  |
| 1523 | [Count Odd Numbers in an Interval Range](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) | Easy | [Python](1523-count-odd-numbers-in-an-interval-range/1523-count-odd-numbers-in-an-interval-range.py) |  |
| 1525 | [Number of Good Ways to Split a String](https://leetcode.com/problems/number-of-good-ways-to-split-a-string/) | Medium | [Python](1525-number-of-good-ways-to-split-a-string/1525-number-of-good-ways-to-split-a-string.py) |  |
| 1527 | [Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/) | Easy | [SQL](1527-patients-with-a-condition/1527-patients-with-a-condition.sql) |  |
| 1528 | [Shuffle String](https://leetcode.com/problems/shuffle-string/) | Easy | [Python](1528-shuffle-string/1528-shuffle-string.py) |  |
| 1550 | [Three Consecutive Odds](https://leetcode.com/problems/three-consecutive-odds/) | Easy | [Python](1550-three-consecutive-odds/1550-three-consecutive-odds.py) |  |
| 1551 | [Minimum Operations to Make Array Equal](https://leetcode.com/problems/minimum-operations-to-make-array-equal/) | Medium | [Python](1551-minimum-operations-to-make-array-equal/1551-minimum-operations-to-make-array-equal.py) |  |
| 1567 | [Maximum Length of Subarray With Positive Product](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/) | Medium | [Python](1567-maximum-length-of-subarray-with-positive-product/1567-maximum-length-of-subarray-with-positive-product.py) |  |
| 1572 | [Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/) | Easy | [Python](1572-matrix-diagonal-sum/1572-matrix-diagonal-sum.py) |  |
| 1578 | [Minimum Time to Make Rope Colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/) | Medium | [Python](1578-minimum-time-to-make-rope-colorful/1578-minimum-time-to-make-rope-colorful.py) |  |
| 1581 | [Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) | Easy | [SQL](1581-customer-who-visited-but-did-not-make-any-transactions/1581-customer-who-visited-but-did-not-make-any-transactions.sql) |  |
| 1587 | [Bank Account Summary II](https://leetcode.com/problems/bank-account-summary-ii/) | Easy | [SQL](1587-bank-account-summary-ii/1587-bank-account-summary-ii.sql) |  |
| 1588 | [Sum Of All Odd Length Subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/) | — | [Python](1588-sum-of-all-odd-length-subarrays/1588-sum-of-all-odd-length-subarrays.py) |  |
| 1603 | [Design Parking System](https://leetcode.com/problems/design-parking-system/) | Easy | [Python](1603-design-parking-system/1603-design-parking-system.py) |  |
| 1605 | [Find Valid Matrix Given Row and Column Sums](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/) | Medium | [Python](1605-find-valid-matrix-given-row-and-column-sums/1605-find-valid-matrix-given-row-and-column-sums.py) |  |
| 1609 | [Even Odd Tree](https://leetcode.com/problems/even-odd-tree/) | Medium | [Python](1609-even-odd-tree/1609-even-odd-tree.py) | [notes](1609-even-odd-tree/NOTES.md) |
| 1636 | [Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) | Easy | [Python](1636-sort-array-by-increasing-frequency/1636-sort-array-by-increasing-frequency.py) |  |
| 1641 | [Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/) | Medium | [Python](1641-count-sorted-vowel-strings/1641-count-sorted-vowel-strings.py) |  |
| 1646 | [Get Maximum in Generated Array](https://leetcode.com/problems/get-maximum-in-generated-array/) | Easy | [Python](1646-get-maximum-in-generated-array/1646-get-maximum-in-generated-array.py) |  |
| 1662 | [Check If Two String Arrays are Equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/) | Easy | [Python](1662-check-if-two-string-arrays-are-equivalent/1662-check-if-two-string-arrays-are-equivalent.py) |  |
| 1667 | [Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/) | Easy | [SQL](1667-fix-names-in-a-table/1667-fix-names-in-a-table.sql) |  |
| 1672 | [Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Easy | [Python](1672-richest-customer-wealth/1672-richest-customer-wealth.py) |  |
| 1678 | [Goal Parser Interpretation](https://leetcode.com/problems/goal-parser-interpretation/) | Easy | [Python](1678-goal-parser-interpretation/1678-goal-parser-interpretation.py) |  |
| 1684 | [Count the Number of Consistent Strings](https://leetcode.com/problems/count-the-number-of-consistent-strings/) | Easy | [Python](1684-count-the-number-of-consistent-strings/1684-count-the-number-of-consistent-strings.py) |  |
| 1688 | [Count of Matches in Tournament](https://leetcode.com/problems/count-of-matches-in-tournament/) | Easy | [Python](1688-count-of-matches-in-tournament/1688-count-of-matches-in-tournament.py) |  |
| 1693 | [Daily Leads and Partners](https://leetcode.com/problems/daily-leads-and-partners/) | Easy | [SQL](1693-daily-leads-and-partners/1693-daily-leads-and-partners.sql) |  |
| 1704 | [Determine if String Halves Are Alike](https://leetcode.com/problems/determine-if-string-halves-are-alike/) | Easy | [Python](1704-determine-if-string-halves-are-alike/1704-determine-if-string-halves-are-alike.py) |  |
| 1729 | [Find Followers Count](https://leetcode.com/problems/find-followers-count/) | Easy | [SQL](1729-find-followers-count/1729-find-followers-count.sql) |  |
| 1741 | [Find Total Time Spent by Each Employee](https://leetcode.com/problems/find-total-time-spent-by-each-employee/) | Easy | [SQL](1741-find-total-time-spent-by-each-employee/1741-find-total-time-spent-by-each-employee.sql) |  |
| 1742 | [Maximum Number of Balls in a Box](https://leetcode.com/problems/maximum-number-of-balls-in-a-box/) | Easy | [Python](1742-maximum-number-of-balls-in-a-box/1742-maximum-number-of-balls-in-a-box.py) |  |
| 1748 | [Sum of Unique Elements](https://leetcode.com/problems/sum-of-unique-elements/) | Easy | [Python](1748-sum-of-unique-elements/1748-sum-of-unique-elements.py) |  |
| 1757 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) | Easy | [SQL](1757-recyclable-and-low-fat-products/1757-recyclable-and-low-fat-products.sql) |  |
| 1768 | [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | Easy | [Python](1768-merge-strings-alternately/1768-merge-strings-alternately.py) |  |
| 1773 | [Count Items Matching a Rule](https://leetcode.com/problems/count-items-matching-a-rule/) | Easy | [Python](1773-count-items-matching-a-rule/1773-count-items-matching-a-rule.py) |  |
| 1779 | [Find Nearest Point That Has the Same X or Y Coordinate](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/) | Easy | [Python](1779-find-nearest-point-that-has-the-same-x-or-y-coordinate/1779-find-nearest-point-that-has-the-same-x-or-y-coordinate.py) |  |
| 1790 | [Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/) | Easy | [Python](1790-check-if-one-string-swap-can-make-strings-equal/1790-check-if-one-string-swap-can-make-strings-equal.py) |  |
| 1795 | [Rearrange Products Table](https://leetcode.com/problems/rearrange-products-table/) | Easy | [SQL](1795-rearrange-products-table/1795-rearrange-products-table.sql) |  |
| 1812 | [Determine Color of a Chessboard Square](https://leetcode.com/problems/determine-color-of-a-chessboard-square/) | Easy | [Python](1812-determine-color-of-a-chessboard-square/1812-determine-color-of-a-chessboard-square.py) |  |
| 1816 | [Truncate Sentence](https://leetcode.com/problems/truncate-sentence/) | Easy | [Python](1816-truncate-sentence/1816-truncate-sentence.py) |  |
| 1822 | [Sign of the Product of an Array](https://leetcode.com/problems/sign-of-the-product-of-an-array/) | Easy | [Python](1822-sign-of-the-product-of-an-array/1822-sign-of-the-product-of-an-array.py) |  |
| 1832 | [Check if the Sentence Is Pangram](https://leetcode.com/problems/check-if-the-sentence-is-pangram/) | Easy | [Python](1832-check-if-the-sentence-is-pangram/1832-check-if-the-sentence-is-pangram.py) |  |
| 1837 | [Sum of Digits in Base K](https://leetcode.com/problems/sum-of-digits-in-base-k/) | Easy | [Python](1837-sum-of-digits-in-base-k/1837-sum-of-digits-in-base-k.py) |  |
| 1844 | [Replace All Digits with Characters](https://leetcode.com/problems/replace-all-digits-with-characters/) | Easy | [Python](1844-replace-all-digits-with-characters/1844-replace-all-digits-with-characters.py) |  |
| 1859 | [Sorting the Sentence](https://leetcode.com/problems/sorting-the-sentence/) | Easy | [Python](1859-sorting-the-sentence/1859-sorting-the-sentence.py) |  |
| 1873 | [Calculate Special Bonus](https://leetcode.com/problems/calculate-special-bonus/) | Easy | [SQL](1873-calculate-special-bonus/1873-calculate-special-bonus.sql) |  |
| 1876 | [Substrings of Size Three with Distinct Characters](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) | Easy | [Python](1876-substrings-of-size-three-with-distinct-characters/1876-substrings-of-size-three-with-distinct-characters.py) |  |
| 1877 | [Minimize Maximum Pair Sum in Array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/) | Medium | [Python](1877-minimize-maximum-pair-sum-in-array/1877-minimize-maximum-pair-sum-in-array.py) |  |
| 1880 | [Check if Word Equals Summation of Two Words](https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/) | Easy | [Python](1880-check-if-word-equals-summation-of-two-words/1880-check-if-word-equals-summation-of-two-words.py) |  |
| 1890 | [The Latest Login in 2020](https://leetcode.com/problems/the-latest-login-in-2020/) | Easy | [SQL](1890-the-latest-login-in-2020/1890-the-latest-login-in-2020.sql) |  |
| 1913 | [Maximum Product Difference Between Two Pairs](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/) | Easy | [Python](1913-maximum-product-difference-between-two-pairs/1913-maximum-product-difference-between-two-pairs.py) |  |
| 1920 | [Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/) | Easy | [Python](1920-build-array-from-permutation/1920-build-array-from-permutation.py) |  |
| 1925 | [Count Square Sum Triples](https://leetcode.com/problems/count-square-sum-triples/) | Easy | [Python](1925-count-square-sum-triples/1925-count-square-sum-triples.py) |  |
| 1929 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy | [Python](concatenation-of-array/concatenation-of-array.py) |  |
| 1935 | [Maximum Number of Words You Can Type](https://leetcode.com/problems/maximum-number-of-words-you-can-type/) | Easy | [Python](1935-maximum-number-of-words-you-can-type/1935-maximum-number-of-words-you-can-type.py) |  |
| 1941 | [Check if All Characters Have Equal Number of Occurrences](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/) | Easy | [Python](1941-check-if-all-characters-have-equal-number-of-occurrences/1941-check-if-all-characters-have-equal-number-of-occurrences.py) |  |
| 1965 | [Employees With Missing Information](https://leetcode.com/problems/employees-with-missing-information/) | Easy | [SQL](1965-employees-with-missing-information/1965-employees-with-missing-information.sql) |  |
| 1967 | [Number of Strings That Appear as Substrings in Word](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/) | Easy | [Python](1967-number-of-strings-that-appear-as-substrings-in-word/1967-number-of-strings-that-appear-as-substrings-in-word.py) |  |
| 1979 | [Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) | Easy | [Python](1979-find-greatest-common-divisor-of-array/1979-find-greatest-common-divisor-of-array.py) |  |
| 2000 | [Reverse Prefix of Word](https://leetcode.com/problems/reverse-prefix-of-word/) | Easy | [Python](2000-reverse-prefix-of-word/2000-reverse-prefix-of-word.py) |  |
| 2006 | [Count Number of Pairs With Absolute Difference K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/) | Easy | [Python](2006-count-number-of-pairs-with-absolute-difference-k/2006-count-number-of-pairs-with-absolute-difference-k.py) |  |
| 2011 | [Final Value of Variable After Performing Operations](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/) | Easy | [Python](2011-final-value-of-variable-after-performing-operations/2011-final-value-of-variable-after-performing-operations.py) |  |
| 2016 | [Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/) | Easy | [Python](2016-maximum-difference-between-increasing-elements/2016-maximum-difference-between-increasing-elements.py) |  |
| 2023 | [Number of Pairs of Strings With Concatenation Equal to Target](https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/) | Medium | [Python](2023-number-of-pairs-of-strings-with-concatenation-equal-to-target/2023-number-of-pairs-of-strings-with-concatenation-equal-to-target.py) |  |
| 2032 | [Two Out of Three](https://leetcode.com/problems/two-out-of-three/) | Easy | [Python](2032-two-out-of-three/2032-two-out-of-three.py) |  |
| 2042 | [Check if Numbers Are Ascending in a Sentence](https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/) | Easy | [Python](2042-check-if-numbers-are-ascending-in-a-sentence/2042-check-if-numbers-are-ascending-in-a-sentence.py) |  |
| 2053 | [Kth Distinct String in an Array](https://leetcode.com/problems/kth-distinct-string-in-an-array/) | Easy | [Python](2053-kth-distinct-string-in-an-array/2053-kth-distinct-string-in-an-array.py) |  |
| 2057 | [Smallest Index With Equal Value](https://leetcode.com/problems/smallest-index-with-equal-value/) | Easy | [Python](2057-smallest-index-with-equal-value/2057-smallest-index-with-equal-value.py) |  |
| 2062 | [Count Vowel Substrings of a String](https://leetcode.com/problems/count-vowel-substrings-of-a-string/) | Easy | [Python](2062-count-vowel-substrings-of-a-string/2062-count-vowel-substrings-of-a-string.py) |  |
| 2073 | [Time Needed to Buy Tickets](https://leetcode.com/problems/time-needed-to-buy-tickets/) | Easy | [Python](2073-time-needed-to-buy-tickets/2073-time-needed-to-buy-tickets.py) |  |
| 2078 | [Two Furthest Houses With Different Colors](https://leetcode.com/problems/two-furthest-houses-with-different-colors/) | Easy | [Python](2078-two-furthest-houses-with-different-colors/2078-two-furthest-houses-with-different-colors.py) |  |
| 2085 | [Count Common Words With One Occurrence](https://leetcode.com/problems/count-common-words-with-one-occurrence/) | Easy | [Python](2085-count-common-words-with-one-occurrence/2085-count-common-words-with-one-occurrence.py) |  |
| 2089 | [Find Target Indices After Sorting Array](https://leetcode.com/problems/find-target-indices-after-sorting-array/) | Easy | [Python](2089-find-target-indices-after-sorting-array/2089-find-target-indices-after-sorting-array.py) |  |
| 2108 | [Find First Palindromic String in the Array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/) | Easy | [Python](2108-find-first-palindromic-string-in-the-array/2108-find-first-palindromic-string-in-the-array.py) |  |
| 2114 | [Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/) | Easy | [Python](2114-maximum-number-of-words-found-in-sentences/2114-maximum-number-of-words-found-in-sentences.py) |  |
| 2119 | [A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/) | Easy | [Python](2119-a-number-after-a-double-reversal/2119-a-number-after-a-double-reversal.py) |  |
| 2124 | [Check if All A's Appears Before All B's](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/) | Easy | [Python](2124-check-if-all-as-appears-before-all-bs/2124-check-if-all-as-appears-before-all-bs.py) |  |
| 2129 | [Capitalize the Title](https://leetcode.com/problems/capitalize-the-title/) | Easy | [Python](2129-capitalize-the-title/2129-capitalize-the-title.py) |  |
| 2133 | [Check if Every Row and Column Contains All Numbers](https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/) | Easy | [Python](2133-check-if-every-row-and-column-contains-all-numbers/2133-check-if-every-row-and-column-contains-all-numbers.py) |  |
| 2154 | [Keep Multiplying Found Values by Two](https://leetcode.com/problems/keep-multiplying-found-values-by-two/) | Easy | [Python](2154-keep-multiplying-found-values-by-two/2154-keep-multiplying-found-values-by-two.py) |  |
| 2160 | [Minimum Sum of Four Digit Number After Splitting Digits](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/) | Easy | [Python](2160-minimum-sum-of-four-digit-number-after-splitting-digits/2160-minimum-sum-of-four-digit-number-after-splitting-digits.py) | [notes](2160-minimum-sum-of-four-digit-number-after-splitting-digits/NOTES.md) |
| 2164 | [Sort Even and Odd Indices Independently](https://leetcode.com/problems/sort-even-and-odd-indices-independently/) | Easy | [Python](2164-sort-even-and-odd-indices-independently/2164-sort-even-and-odd-indices-independently.py) | [notes](2164-sort-even-and-odd-indices-independently/NOTES.md) |
| 2169 | [Count Operations to Obtain Zero](https://leetcode.com/problems/count-operations-to-obtain-zero/) | Easy | [Python](2169-count-operations-to-obtain-zero/2169-count-operations-to-obtain-zero.py) |  |
| 2176 | [Count Equal and Divisible Pairs in an Array](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/) | Easy | [Python](2176-count-equal-and-divisible-pairs-in-an-array/2176-count-equal-and-divisible-pairs-in-an-array.py) |  |
| 2180 | [Count Integers With Even Digit Sum](https://leetcode.com/problems/count-integers-with-even-digit-sum/) | Easy | [Python](2180-count-integers-with-even-digit-sum/2180-count-integers-with-even-digit-sum.py) |  |
| 2181 | [Merge Nodes in Between Zeros](https://leetcode.com/problems/merge-nodes-in-between-zeros/) | Medium | [Python](2181-merge-nodes-in-between-zeros/2181-merge-nodes-in-between-zeros.py) |  |
| 2185 | [Counting Words With a Given Prefix](https://leetcode.com/problems/counting-words-with-a-given-prefix/) | Easy | [Python](2185-counting-words-with-a-given-prefix/2185-counting-words-with-a-given-prefix.py) |  |
| 2194 | [Cells in a Range on an Excel Sheet](https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/) | Easy | [Python](2194-cells-in-a-range-on-an-excel-sheet/2194-cells-in-a-range-on-an-excel-sheet.py) |  |
| 2206 | [Divide Array Into Equal Pairs](https://leetcode.com/problems/divide-array-into-equal-pairs/) | Easy | [Python](2206-divide-array-into-equal-pairs/2206-divide-array-into-equal-pairs.py) |  |
| 2215 | [Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) | Easy | [Python](2215-find-the-difference-of-two-arrays/2215-find-the-difference-of-two-arrays.py) |  |
| 2220 | [Minimum Bit Flips to Convert Number](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/) | Easy | [Python](2220-minimum-bit-flips-to-convert-number/2220-minimum-bit-flips-to-convert-number.py) |  |
| 2221 | [Find Triangular Sum of an Array](https://leetcode.com/problems/find-triangular-sum-of-an-array/) | Medium | [Python](2221-find-triangular-sum-of-an-array/2221-find-triangular-sum-of-an-array.py) |  |
| 2235 | [Add Two Integers](https://leetcode.com/problems/add-two-integers/) | — | [Python](2235-add-two-integers/2235-add-two-integers.py) |  |
| 2236 | [Root Equals Sum of Children](https://leetcode.com/problems/root-equals-sum-of-children/) | Easy | [Python](2236-root-equals-sum-of-children/2236-root-equals-sum-of-children.py) |  |
| 2248 | [Intersection of Multiple Arrays](https://leetcode.com/problems/intersection-of-multiple-arrays/) | Easy | [Python](2248-intersection-of-multiple-arrays/2248-intersection-of-multiple-arrays.py) |  |
| 2255 | [Count Prefixes of a Given String](https://leetcode.com/problems/count-prefixes-of-a-given-string/) | Easy | [Python](2255-count-prefixes-of-a-given-string/2255-count-prefixes-of-a-given-string.py) |  |
| 2264 | [Largest 3-Same-Digit Number in String](https://leetcode.com/problems/largest-3-same-digit-number-in-string/) | Easy | [Python](2264-largest-3-same-digit-number-in-string/2264-largest-3-same-digit-number-in-string.py) |  |
| 2265 | [Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/) | Medium | [Python](2265-count-nodes-equal-to-average-of-subtree/2265-count-nodes-equal-to-average-of-subtree.py) |  |
| 2266 | [Count Number of Texts](https://leetcode.com/problems/count-number-of-texts/) | Medium | [Python](2266-count-number-of-texts/2266-count-number-of-texts.py) |  |
| 2267 | [Check if There Is a Valid Parentheses String Path](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/) | Hard | [Python](2267-check-if-there-is-a-valid-parentheses-string-path/2267-check-if-there-is-a-valid-parentheses-string-path.py) |  |
| 2269 | [Find the K-Beauty of a Number](https://leetcode.com/problems/find-the-k-beauty-of-a-number/) | Easy | [Python](2269-find-the-k-beauty-of-a-number/2269-find-the-k-beauty-of-a-number.py) |  |
| 2270 | [Number of Ways to Split Array](https://leetcode.com/problems/number-of-ways-to-split-array/) | Medium | [Python](2270-number-of-ways-to-split-array/2270-number-of-ways-to-split-array.py) |  |
| 2278 | [Percentage of Letter in String](https://leetcode.com/problems/percentage-of-letter-in-string/) | Easy | [Python](2278-percentage-of-letter-in-string/2278-percentage-of-letter-in-string.py) |  |
| 2283 | [Check if Number Has Equal Digit Count and Digit Value](https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/) | Easy | [Python](2283-check-if-number-has-equal-digit-count-and-digit-value/2283-check-if-number-has-equal-digit-count-and-digit-value.py) |  |
| 2284 | [Sender With Largest Word Count](https://leetcode.com/problems/sender-with-largest-word-count/) | Medium | [Python](2284-sender-with-largest-word-count/2284-sender-with-largest-word-count.py) |  |
| 2285 | [Maximum Total Importance of Roads](https://leetcode.com/problems/maximum-total-importance-of-roads/) | Medium | [Python](2285-maximum-total-importance-of-roads/2285-maximum-total-importance-of-roads.py) |  |
| 2299 | [Strong Password Checker II](https://leetcode.com/problems/strong-password-checker-ii/) | Easy | [Python](2299-strong-password-checker-ii/2299-strong-password-checker-ii.py) |  |
| 2309 | [Greatest English Letter in Upper and Lower Case](https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/) | Easy | [Python](2309-greatest-english-letter-in-upper-and-lower-case/2309-greatest-english-letter-in-upper-and-lower-case.py) |  |
| 2325 | [Decode the Message](https://leetcode.com/problems/decode-the-message/) | Easy | [Python](2325-decode-the-message/2325-decode-the-message.py) |  |
| 2341 | [Maximum Number of Pairs in Array](https://leetcode.com/problems/maximum-number-of-pairs-in-array/) | Easy | [Python](2341-maximum-number-of-pairs-in-array/2341-maximum-number-of-pairs-in-array.py) |  |
| 2351 | [First Letter to Appear Twice](https://leetcode.com/problems/first-letter-to-appear-twice/) | Easy | [Python](2351-first-letter-to-appear-twice/2351-first-letter-to-appear-twice.py) |  |
| 2352 | [Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/) | Medium | [Python](2352-equal-row-and-column-pairs/2352-equal-row-and-column-pairs.py) |  |
| 2357 | [Make Array Zero by Subtracting Equal Amounts](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/) | Easy | [Python](2357-make-array-zero-by-subtracting-equal-amounts/2357-make-array-zero-by-subtracting-equal-amounts.py) |  |
| 2363 | [Merge Similar Items](https://leetcode.com/problems/merge-similar-items/) | Easy | [Python](2363-merge-similar-items/2363-merge-similar-items.py) |  |
| 2367 | [Number of Arithmetic Triplets](https://leetcode.com/problems/number-of-arithmetic-triplets/) | Easy | [Python](2367-number-of-arithmetic-triplets/2367-number-of-arithmetic-triplets.py) |  |
| 2396 | [Strictly Palindromic Number](https://leetcode.com/problems/strictly-palindromic-number/) | Medium | [Python](2396-strictly-palindromic-number/2396-strictly-palindromic-number.py) |  |
| 2405 | [Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/) | Medium | [Python](2405-optimal-partition-of-string/2405-optimal-partition-of-string.py) |  |
| 2413 | [Smallest Even Multiple](https://leetcode.com/problems/smallest-even-multiple/) | Easy | [Python](2413-smallest-even-multiple/2413-smallest-even-multiple.py) |  |
| 2418 | [Sort the People](https://leetcode.com/problems/sort-the-people/) | Easy | [Python](2418-sort-the-people/2418-sort-the-people.py) |  |
| 2427 | [Number of Common Factors](https://leetcode.com/problems/number-of-common-factors/) | Easy | [Python](2427-number-of-common-factors/2427-number-of-common-factors.py) |  |

</details>
<!-- INDEX:END -->

### Reference
- [LeetHub: Linking GitHub and LeetCode](https://github.com/QasimWani/LeetHub) — what syncs the statements into this repo
