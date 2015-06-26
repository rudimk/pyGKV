# pyGKV
Experimental Python bindings for gkv.

[Gkv](https://github.com/ybur-yug/gkv) happens to be a neat key-value store using Git. pyGKV is an experimental Python library for using gkv from within your Python modules.

## Internals

Nothing special, for now. pyGKV uses the [Rython](https://github.com/mjpizz/rython) library to create an XML-RPC interface to a Ruby interpreter. It also marshalls Ruby datatypes to Python types, and vice versa. Neat stuff, eh?

## Getting started

- Clone this repo, and install dependencies. Also make sure you've got gkv installed.

```bash
git clone https://github.com/rudimk/pyGKV.git
pip install -r requirements.txt
gem install gkv
```

- Import the library into your namespace.

```python
import pygkv
```

- Initialize a gkv store.

```python
db = pygkv.init_gkv()
```

- Now you're all set! 

```python
db.set("apples", 12)
db.set("oranges", 13)
db.get("apples")
db.all()
```
