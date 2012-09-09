# -*- coding: utf-8 -*-
from __future__ import absolute_import
from .persistence import Persistence
from .memory import MemoryPersistence


class EmbeddedPersistence(Persistence):
    """
    Persistence wrapper that uses a list of embedded entries.
    """

    def __init__(self, parent, parent_query, field):
        self.parent = parent
        self.parent_query = parent_query
        self.field = field
        self.parent_inst = self.parent.read_one(self.parent_query)
        self.l = self.parent_inst[field]

    def create(self, data):
        self.l.append(data)
        self.parent.update(self.parent_query, {self.field: self.l})
        return True

    def read_many(self, query, fields=None, skip=0, limit=0):
        return MemoryPersistence(self.l).read_many(query, fields, skip, limit)

    def read_one(self, query, fields=None):
        return MemoryPersistence(self.l).read_one(query, fields)

    def _replace_parent(self, mp):
        self.l = mp.db
        self.parent.update(self.parent_query, {self.field: self.l})

    def replace(self, query, params):
        mp = MemoryPersistence(self.l)
        r = mp.replace(query, params)
        self._replace_parent(mp)
        return True

    def update(self, query, params):
        mp = MemoryPersistence(self.l)
        r = mp.update(query, params)
        self._replace_parent(mp)
        return True

    def delete(self, query):
        mp = MemoryPersistence(self.l)
        r = mp.delete(query)
        self._replace_parent(mp)
        return True

    def count(self):
        return len(self.parent.read_one(self.parent_query)[self.field])
