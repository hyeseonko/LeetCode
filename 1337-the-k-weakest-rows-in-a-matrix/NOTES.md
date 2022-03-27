### Approach 1
```
return [v for _, v in sorted([(sum(m), i) for i, m in enumerate(mat)])[:k]]
```