
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('smriti.html')

# @app.route('/market_cap', methods = ["POST","GET"])
# def market_cap():


if __name__ == "__main__":
    app.run(debug = True)