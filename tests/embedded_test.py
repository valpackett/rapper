# -*- coding: utf-8 -*-
import t
from should_dsl import *
from rapper import (
    MemoryPersistence,
    EmbeddedPersistence
)


class EmbeddedTest(t.Test):

    def setUp(self):
        mp = MemoryPersistence()
        mp.create({"name": "one", "embed": []})
        self.p = EmbeddedPersistence(mp, {"name": "one"}, "embed")
