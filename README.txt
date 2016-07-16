Shih Yu Chang
W205 Storing and Retrieving Data - Exercise 2
July 16th, 2016

#### Step-by-step instructions for application execution ####

- Ensure that postgres is running
- Use the following commands to login to postgres as user ・postgres・, create a postgres database called ・count・, and a table, within the ・count・ database, called ．tweetwordcount・:

psql -U postgres
CREATE DATABASE tcount;
\connect tcount
CREATE TABLE tweetwordcount;

- Exit postgres using: \q 

Postgres DB summary - the following must be correct for successful application execution:
database="tcount"
table=：tweetwordcount；
user="postgres"
password="pass"
host="localhost"
port="5432"

- Navigate to the directory ．EX2Tweetwordcount・
- Eexecute command ．sparse run・ 
- Allow the process to run during the process of extracting word counts from the Twitter stream. 
- Enter Ctrl-C to stop the application

- To query the data acquired during application execution, either (1) login to postgres, access the database and table, and execute appropriate SQL queries, or (2) use finalresults.py and histogram.py as follows:

For finalresults.py , this script gets a word as an argument and returns the total number of word
occurrences captured in the tweet stream. Example execution:
$ python finalresults.py hello
$ Total number of occurrences of ：hello；: 2

If executed without an argument, this script returns all the words in the stream and their total occurrences, sorted alphabetically, one word per line. Example execution:
$ python finalresults.py
$ the  14
$ a  16
$ at  1
$ be  12

For histogram.py, this script gets two integers and returns all the words for which total occurrences in the tweet stream falls in the range between the integers, inclusively. Note, there should be a space, instead of comma, between range numbers. Example:
$ python histogram.py 3 8
$ what 8
$ with 3
$ why 6
  

