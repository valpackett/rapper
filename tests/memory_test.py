# -*- coding: utf-8 -*-
import t
from should_dsl import *
from rapper import MemoryPersistence


class MemoryTest(t.Test):

    def setUp(self):
        self.p = MemoryPersistence()
