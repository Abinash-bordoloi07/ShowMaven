from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/venues', methods=['GET'])
def get_venues():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM venues')
    venues = c.fetchall()
    conn.close()
    return jsonify(venues)

@app.route('/shows', methods=['GET'])
def get_shows():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM shows')
    shows = c.fetchall()
    conn.close()
    return jsonify(shows)

@app.route('/venues', methods=['POST'])
def create_venue():
    data = request.get_json()
    name = data['name']
    place = data['place']
    capacity = data['capacity']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO venues (name, place, capacity) VALUES (?, ?, ?)', (name, place, capacity))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Venue created successfully'})

@app.route('/shows', methods=['POST'])
def create_show():
    data = request.get_json()
    name = data['name']
    rating = data['rating']
    tags = data['tags']
    ticket_price = data['ticket_price']
    venue_id = data['venue_id']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO shows (name, rating, tags, ticket_price, venue_id) VALUES (?, ?, ?, ?, ?)', (name, rating, tags, ticket_price, venue_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Show created successfully'})

if __name__ == '__main__':
    app.run(debug=True)
