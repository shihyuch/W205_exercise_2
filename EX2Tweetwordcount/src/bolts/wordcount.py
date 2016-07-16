from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
# from redis import StrictRedis


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        # self.redis = StrictRedis()

    def process(self, tup):
        word = tup.values[0]

        # Increment the local count
        self.counts[word] += 1

        # Output count to screen log
        self.log('%s: %d' % (word, self.counts[word]))

        # Log count in database 
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
        if self.counts[word] == 1:  # See first word, insert into database
            cur.execute("insert into tweetwordcount (word, count) values (%s, %s)", (word, self.counts[word]))
        else:                       # Database updating 
            cur.execute("update tweetwordcount set count=%s where word=%s", (self.counts[word], word))
        conn.commit()
        conn.close()

        # Emit word / count
        self.emit([word, self.counts[word]])
