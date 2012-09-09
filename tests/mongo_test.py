# -*- coding: utf-8 -*-
import t
import pymongo
from should_dsl import *
from rapper import MongoPersistence


class MongoTest(t.Test):

    def setUp(self):
        self.m = pymongo.Connection()["rapper_test"]
        self.p = MongoPersistence(self.m, "test")

    def tearDown(self):
        self.m["test"].drop()

    def test_objectid(self):
        self.p.create({"a": "b"})
        self.p.read_one({"a": "b"})["_id"] |should_be.kind_of| str
        self.p.read_many({"a": "b"})[0]["_id"] |should_be.kind_of| str
