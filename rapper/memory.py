# -*- coding: utf-8 -*-
from __future__ import absolute_import
from .persistence import Persistence


class MemoryPersistence(Persistence):

    "In-memory list persistence adapter"

    def __init__(self, db=None):
        self.db = db
        if not db:
            self.db = []

    def matches(self, d, query):
        for key, qval in query.iteritems():
            dval = d[key]
            if type(dval) == dict and not self.matches(dval, qval):
                return False
            if dval != qval:
                return False
        return True

    def create(self, params):
        self.db.append(params)
        return True

    def read_many(self, query, fields=None, skip=0, limit=0):
        if limit == 0:
            limit = len(self.db)
        result = [d for d in self.db[skip:][:limit] if self.matches(d, query)]
        if fields:
            result = [dict([(k, v) for k, v in d.iteritems() if k in fields])
                    for d in result]
        return result

    def read_one(self, query, fields=None):
        try:
            return self.read_many(query, fields)[0].copy()
        except IndexError:
            return None

    def replace(self, query, params):
        self.db = [params if self.matches(d, query) else d for d in self.db]
        return True

    def update(self, query, params):
        self.db = [dict(d.items() + params.items()) if self.matches(d, query)
                else d for d in self.db]
        return True

    def delete(self, query):
        self.db = filter(lambda d: not self.matches(d, query), self.db)
        return True

    def count(self):
        return len(self.db)
