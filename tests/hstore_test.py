# -*- coding: utf-8 -*-
import t
import os
import psycopg2
from should_dsl import *
from rapper import HstorePersistence


class HstoreTest(t.Test):

    def setUp(self):
        connstr = "host=127.0.0.1 port=5432 dbname=rapper_test"
        if os.environ.get("CI"):
            connstr += " user=postgres"
        self.c = psycopg2.connect(connstr)
        self.c.cursor().execute("create table test (id serial primary key, data hstore)")
        self.c.commit()
        self.p = HstorePersistence(self.c, "test")

    def tearDown(self):
        self.c.cursor().execute("drop table test")
        self.c.commit()
