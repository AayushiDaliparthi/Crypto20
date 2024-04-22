import pandas as pd
import psycopg2
from psycopg2 import sql

PGEND_POINT = 'database-1.chueoayw4q5g.ca-central-1.rds.amazonaws.com' # End_point
PGDATABASE_NAME = 'Crypto20_db' # Database Name example: youtube_test_db
PGUSER_NAME = 'postgres' # UserName
PGPASSWORD = '12345678' # Password

def connect():
    
    # Set up a connection to the postgres server.
    conn_string = "host="+ PGEND_POINT +" port="+ "5432" +" dbname="+ PGDATABASE_NAME +" user=" + PGUSER_NAME \
                  +" password="+ PGPASSWORD
    
    conn = psycopg2.connect(conn_string)
    print("Connected!")

    # Create a cursor object
    cursor = conn.cursor()
    
    return conn, cursor

conn, cursor = connect()

# Creating simple table
query_menu = sql.SQL("""
SELECT * FROM public."Avalanche"
ORDER BY "Date" ASC LIMIT 100
""")
cur = conn.cursor()
cur.execute(query_menu)
print(cur.fetchall())