# pyGKV
Experimental Python bindings for gkv.

[Gkv](https://github.com/ybur-yug/gkv) happens to be a neat key-value store using Git. pyGKV is an experimental Python library for using gkv from within your Python modules.

## Getting started

1. Clone this repo. 

2. Import the library into your namespace.

```python
import pygkv
```

3. Initialize a gkv store.

```python
db = pygkv.init_gkv()
```

4. Now you're all set! 

```python
db.set("apples", 12)
db.set("oranges", 13)
db.get("apples")
db.all()
```
