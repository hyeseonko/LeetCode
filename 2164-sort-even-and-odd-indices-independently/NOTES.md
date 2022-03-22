### Technique
How to insert items from two lists in an alternating manner.
```python
# two lists = even, odd
output = [None]*(len(even)+len(odd))
output[::2]=even
output[1::2]=odd
```