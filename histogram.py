import psycopg2
import sys
import re

k1 = int(sys.argv[1])
k2 = int(sys.argv[2])

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("SELECT * FROM tweetwordcount")
records = cur.fetchall()
records = list(set(records)) # remove duplicate

# store all records with counts between k1 and k2
result_records = []
for rec in records:
    if k1 <= rec[1] <= k2:
        result_records.append(rec)

# output satisfied records
for item in result_records:
    print(item)

conn.commit()
conn.close()
