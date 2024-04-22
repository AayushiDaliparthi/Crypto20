import pandas as pd
import psycopg2
from psycopg2 import sql
import matplotlib.pyplot as plt
import seaborn as sns

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

# Execute SQL query to fetch data from the database for Binance
query_binance = sql.SQL("""
    SELECT * FROM public."Binance"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Bitcoin
query_bitcoin = sql.SQL("""
    SELECT * FROM public."Bitcoin"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Bitcoin_cash
query_bitcoin_cash = sql.SQL("""
    SELECT * FROM public."Bitcoin_cash"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Cardano
query_Cardano = sql.SQL("""
    SELECT * FROM public."Cardano"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Chainlink
query_Chainlink = sql.SQL("""
    SELECT * FROM public."Chainlink"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Ethereum
query_ethereum = sql.SQL("""
    SELECT * FROM public."Ethereum"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Polkadot
query_Polkadot = sql.SQL("""
    SELECT * FROM public."Polkadot"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Polygon
query_Polygon = sql.SQL("""
    SELECT * FROM public."Polygon"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Solana
query_Solana = sql.SQL("""
    SELECT * FROM public."Solana"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Tether
query_tether = sql.SQL("""
    SELECT * FROM public."Tether"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Wrapped_Bitcoin
query_Wrapped_Bitcoin = sql.SQL("""
    SELECT * FROM public."Wrapped_Bitcoin"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Wrapped_TRON
query_Wrapped_TRON = sql.SQL("""
    SELECT * FROM public."Wrapped_TRON"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for Toncoin
query_Toncoin = sql.SQL("""
    SELECT * FROM public."Toncoin"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for dodge
query_dodge = sql.SQL("""
    SELECT * FROM public."dodge"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for shiba_inu
query_shiba_inu = sql.SQL("""
    SELECT * FROM public."shiba_inu"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for steth
query_steth = sql.SQL("""
    SELECT * FROM public."steth"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for tron
query_tron = sql.SQL("""
    SELECT * FROM public."tron"
    ORDER BY "Date" ASC
    LIMIT 100
""")

# Execute SQL query to fetch data from the database for usdc_coin
query_usdc_coin = sql.SQL("""
    SELECT * FROM public."usdc_coin"
    ORDER BY "Date" ASC
    LIMIT 100
""")
cur = conn.cursor()
cur.execute(query_menu)
rows = print(cur.fetchall())


