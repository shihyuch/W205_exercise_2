
import psycopg2
import sys

k1 = int(sys.argv[1])
k2 = int(sys.argv[2])

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("SELECT * FROM tweetwordcount")
records = cur.fetchall()
records = list(set(records)) # consider for repeating records

# store all records with counts between k1 and k2
final_records = []
for rec in records:
   if k1 <= rec[1] <= k2:
      final_records.append(rec)  

# output stored records
col_width = max(len(str(item)) for record in final_records for item in record) + 1
for rec in final_records:
    print "".join(str(item).ljust(col_width) for item in rec)

conn.commit()
conn.close()

