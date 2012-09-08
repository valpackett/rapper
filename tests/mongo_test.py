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
