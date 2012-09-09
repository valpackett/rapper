# -*- coding: utf-8 -*-
from __future__ import absolute_import
from .persistence import Persistence


class MongoPersistence(Persistence):

    "PyMongo persistence adapter"

    def __init__(self, mongo, collection):
        self.db = mongo[collection]

    def create(self, params):
        objid = self.db.insert(params)
        return True

    def read_one(self, query, **kwargs):
        d = self.db.find_one(query, **kwargs)
        if d:
            if not "fields" in kwargs:
                kwargs["fields"] = ["_id"]
            if "_id" in kwargs["fields"]:
                d["_id"] = str(d["_id"])
            else:
                del d["_id"]
        return d

    def read_many(self, query, **kwargs):
        c = [d for d in self.db.find(query, **kwargs)]
        if not "fields" in kwargs:
            kwargs["fields"] = ["_id"]
        if "_id" in kwargs["fields"]:
            for d in c:
                d["_id"] = str(d["_id"])
        else:
            for d in c:
                del d["_id"]
        return c

    def replace(self, query, params):
        self.db.update(query, params)
        return True

    def update(self, query, params):
        self.db.update(query, {"$set": params})
        return True

    def delete(self, query):
        self.db.remove(query)
        return True

    def count(self):
        return self.db.count()
