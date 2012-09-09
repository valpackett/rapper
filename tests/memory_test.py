# -*- coding: utf-8 -*-
import t
from should_dsl import *
from rapper import MemoryPersistence


class MemoryTest(t.Test):

    def setUp(self):
        self.p = MemoryPersistence()

    def test_matches(self):
        self.p.matches({"a": {"b": 1}}, {"a": {"b": 2}}) |should_be.equal_to| False
