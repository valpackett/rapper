# rapper

RapPer (Rapid Persistence) is a unified interface for storing data in different databases.
Extracted from [RapidMachine](https://github.com/myfreeweb/rapidmachine).

```python
>>> from rapper import MemoryPersistence
>>> p = MemoryPersistence()
>>>
>>> p.create({"name": "one", "text": "Hello world", "views": "100"})
>>> p.create({"name": "two", "text": "Hello world", "views": "100"})
>>> p.read_one({"name": "one"})
{"name": "one", "text": "Hello world", "views": "100"}
>>> p.read_many({"views": "100"})
[{"name": "one", "text": "Hello world", "views": "100"}, {"name": "two", "text": "Hello world", "views": "100"}]

>>> p.update({"name": "one"}, {"views", "101"})
>>> p.read_one({"name": "one"})
{"name": "one", "text": "Hello world", "views": "101"}

>>> p.replace({"name": "one"}, {"name": "one", "link": "floatboth.com", "views": "10"})
>>> p.read_one({"name": "one"})
{"name": "one", "link": "floatboth.com", "views": "10"}

>>> p.delete({"name": "one"})
```
