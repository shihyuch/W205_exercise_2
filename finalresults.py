import psycopg2
import sys
import re

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(sys.argv) > 1:
    word = sys.argv[1]
    SQLstatement = "SELECT count FROM tweetwordcount WHERE word='%s'" % word
    cur.execute(SQLstatement)
    records = cur.fetchall()
    records = list(set(records))   # removing duplicate
    try:
        print "Total number of occurences of " + word + ": " + str(records[0][0])
    except IndexError:
        print "Total number of occurences of " + word + ": 0"
else:
    cur.execute("SELECT * FROM tweetwordcount")
    records = cur.fetchall()
    records = list(set(records)) #  removing duplicate
    records.sort()
    for item in records:
        print(item)

conn.commit()
conn.close()
