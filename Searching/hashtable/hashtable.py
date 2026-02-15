""" MAP ADT
Since a map stores a collection of objects, it should be viewed as a collection of
key-value pairs. As an ADT, a map M supports the following methods:
size(): Returns the number of entries in M.
isEmpty(): Returns a boolean indicating whether M is empty.
get(k): Returns the value v associated with key k, if such an entry exists;
otherwise returns null.
put(k, v): If M does not have an entry with key equal to k, then adds entry
(k,v) to M and returns null; else, replaces with v the existing
value of the entry with key equal to k and returns the old value.
remove(k): Removes from M the entry with key equal to k, and returns its
value; if M has no such entry, then returns null.
keySet(): Returns an iterable collection containing all the keys stored in M.
values(): Returns an iterable collection containing all the values of entries
stored in M (with repetition if multiple keys map to the same
value).
entrySet(): Returns an iterable collection containing all the key-value en
tries in M.
"""
from dataclasses import dataclass
import typing
from hashlib import sha256, md5

@dataclass
class Entry:
    __slots__ = ("_key", "_value")
    _key: typing.Any
    _value: typing.Any
    
    @property
    def key(self) -> typing.Any:
        return self._key
    
    @property
    def value(self) -> typing.Any:
        return self._value
    
    def __repr__(self) -> str:
        return f"<Entry>: {self.key}: {self.value}"

class HashTable:

    DEFAULT_SIZE: int = 8

    def __init__(self, size: int = DEFAULT_SIZE) -> None:
        self.table: list[Entry] = [None] * size
    
    def _hash(self, key: typing.Any) -> int:
        return int(sha256(str(key).encode("utf-8")).hexdigest(), 16) % len(self.table)
        
    def size(self) -> int:
        return sum(1 for _ in filter(None, self.table))

    def is_empty(self) -> bool:
        return sum(1 for i in self.table if i != None) == 0
    
    
    def get(self, key: typing.Any) -> typing.Any | None:
        key_hash: int = self._hash(key)
        entry: Entry | None = self.table[key_hash] if self.table[key_hash] else None
        return entry.value if entry else None
    
    def put(self, key: typing.Any, value: typing.Any) -> typing.Any | None:
        key_hash: int = self._hash(key)
        entry: Entry = Entry(key, value)
        _old_value = self.table[key_hash].value if self.table[key_hash] else None
        self.table[key_hash] = entry
        return _old_value
    
    def remove(self, key: typing.Any) -> typing.Any | None:
        key_hash: int = self._hash(key)
        _val: typing.Any = None
        if self.table[key_hash]:
            _val = self.table[key_hash].value
            self.table[key_hash] = None
        return _val
    
    def key_set(self) -> list[typing.Any]:
        return [e.key for e in (filter(None, self.table))]
    
    def values(self) -> list[typing.Any]:
        return [e.value for e in (filter(None, self.table))]
    
    def items(self) -> list[typing.Any]:
        return [(e.key, e.value) for e in (filter(None, self.table))]
        


