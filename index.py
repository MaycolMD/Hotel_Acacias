from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/booking')
def reserva():
    return render_template('booking.html')

@app.route('/search')
def search():
    return render_template('roomsearch.html')

if __name__ == '__main__':
    app.run(debug=True)