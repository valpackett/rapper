# -*- coding: utf-8 -*-
import unittest
from should_dsl import *


def drange(minn, maxx):
    return [{"i": str(i)} for i in range(minn, maxx)]


class Test(unittest.TestCase):

    def test_create_read_count(self):
        d = {"name": "creation", "val": "something"}
        self.p.create(d.copy()) |should_be.equal_to| True
        r = self.p.read_one({"name": "creation"}, fields=["name", "val"])
        r |should_be.equal_to| d
        self.p.count() |should_be.equal_to| 1

    def test_read_fail(self):
        self.p.read_one({"name": "nothing"}) |should_be.equal_to| None

    def test_skip(self):
        for i in range(0, 10):
            self.p.create({"i": str(i)})
        self.p.read_many({}, skip=5, fields=["i"]) |should_be.equal_to| drange(5, 10)

    def test_limit(self):
        for i in range(0, 10):
            self.p.create({"i": str(i)})
        self.p.read_many({}, limit=5, fields=["i"]) |should_be.equal_to| drange(0, 5)

    def test_delete(self):
        self.p.create({"name": "deletion", "val": "something"})
        self.p.count() |should_be.equal_to| 1
        self.p.delete({"val": "something"}) |should_be.equal_to| True
        self.p.count() |should_be.equal_to| 0

    def test_replace(self):
        r = {"name": "replaced", "two": "3"}
        self.p.create({"name": "replacement", "one": "1", "two": "2"})
        self.p.replace({"one": "1"}, r) |should_be.equal_to| True
        self.p.read_one({"two": "3"}, fields=["name", "one", "two"]) |should_be.equal_to| r

    def test_update(self):
        self.p.create({"name": "updating", "id": "1"})
        self.p.update({"id": "1"}, {"uid": "12"}) |should_be.equal_to| True
        self.p.read_one({"id": "1"}, fields=["name", "id", "uid"]) |should_be.equal_to| {
            "name": "updating", "id": "1", "uid": "12"
        }
