import psycopg2
import sys

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(sys.argv) > 1:
    word = sys.argv[1]
    statement = "SELECT count FROM tweetwordcount WHERE word='%s'" % word
    cur.execute(statement)
    records = cur.fetchall()
    records = list(set(records))   # consider for repeating records
    try:
        print "Total number of occurences of " + word + ": " + str(records[0][0])
    except IndexError:
        print "Total number of occurences of " + word + ": 0"
else:
    cur.execute("SELECT * FROM tweetwordcount")
    records = cur.fetchall()
    records = list(set(records)) # consider for repeating records
    records.sort()
    col_width = max(len(str(item)) for record in records for item in record) + 1
    for rec in records:
       print "".join(str(item).ljust(col_width) for item in rec)

conn.commit()
conn.close()
