# -*- coding: utf-8 -*-


class Persistence(object):  # pragma: no cover

    """
    Basic persistence interface.

    All methods here (except __init__) just raise NotImplemented.
    Use one of its subclasses or make your own.
    """

    def __init__(self):
        pass

    def create(self, params):
        "Creates an object in the database."
        raise NotImplemented()

    def read_one(self, query, fields=None):
        "Reads one object from the database."
        raise NotImplemented()

    def read_many(self, query, fields=None, skip=0, limit=0):
        "Reads many objects from the database."
        raise NotImplemented()

    def replace(self, query, params):
        "Replaces an object in the database."
        raise NotImplemented()

    def update(self, query, params):
        "Updates an object in the database."
        raise NotImplemented()

    def delete(self, query):
        "Deletes an object in the database."
        raise NotImplemented()

    def count(self):
        "Returns how much there are objects in the database."
        raise NotImplemented()
