### How to create alphabet:num dictionary
```python
di=dict(zip([ord(c)%32 for c in string.ascii_lowercase], string.ascii_lowercase))
```