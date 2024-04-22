import pandas as pd
import psycopg2
from psycopg2 import sql
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
from flask import Flask, render_template

# PostgreSQL database connection details
PGEND_POINT = 'database-1.chueoayw4q5g.ca-central-1.rds.amazonaws.com'
PGDATABASE_NAME = 'Crypto20_db'
PGUSER_NAME = 'postgres'
PGPASSWORD = '12345678'

# Function to establish a connection to the PostgreSQL database
def connect():
    conn_string = "host="+ PGEND_POINT +" port="+ "5432" +" dbname="+ PGDATABASE_NAME +" user=" + PGUSER_NAME \
                  +" password="+ PGPASSWORD
    conn = psycopg2.connect(conn_string)
    print("Connected!")
    cursor = conn.cursor()
    return conn, cursor

# Flask app initialization
app = Flask(__name__)

# Route to display the opening price plot and correlation heatmap
@app.route('/')
def index():
    # Establish connection to PostgreSQL database
    conn, cursor = connect()
    
    # Query PostgreSQL database for Avalanche data
    query_menu = sql.SQL("""
    SELECT * FROM public."Avalanche"
    ORDER BY "Date" ASC LIMIT 100
    """)
    cursor.execute(query_menu)
    avalanche_data = cursor.fetchall()

    # Plot opening price for top 10 cryptocurrencies
    plt.figure(figsize=(17, 9))
    for coin in [Bitcoin, Ethereum, Tether, Binance, Solana, xrp, steth, usd_coin, dodge, Toncoin]:
        coin['Open'].plot(label=coin.name)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Opening Price of Top 10 Cryptocurrencies (Past Decade)')
    plt.legend()
    opening_price_plot_path = 'static/opening_price_plot.png'
    plt.savefig(opening_price_plot_path)

    # Plot correlation heatmap
    combined_data = pd.concat([Bitcoin['Open'], Ethereum['Open'], Tether['Open'], Binance['Open'], Solana['Open'],
                               xrp['Open'], steth['Open'], usd_coin['Open'], dodge['Open'], Toncoin['Open']], axis=1)
    combined_data.columns = ['Bitcoin', 'Ethereum', 'Tether', 'Binance', 'Solana', 'XRP', 'STETH', 'USDC', 'DOGE', 'TON']
    correlation_matrix = combined_data.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap of Top 10 Cryptocurrencies Opening Price')
    heatmap_plot_path = 'static/heatmap_plot.png'
    plt.savefig(heatmap_plot_path)

    return render_template('index.html', opening_price_plot_path=opening_price_plot_path, 
                           heatmap_plot_path=heatmap_plot_path, avalanche_data=avalanche_data)

if __name__ == '__main__':
    app.run(debug=True)
